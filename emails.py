import csv
import re
# Function to read the input file and return a list of tuples (email, last_name)
def read_input_file(filename, university_name, specialty1, specialty2):
    with open(filename, 'r') as file:
        final_data = []
        num_duplicate = 0
        num_false_data = 0
        num_true_data = 0
        
        csvreader = csv.reader(file)
        # Skip the header row
        next(csvreader)
        
        # Construct regex patterns for email, name, university, and specialties
        university_pattern = rf'\b{re.escape(university_name)}\b'
        specialty_pattern = rf'\b({re.escape(specialty1)}|{re.escape(specialty2)})\b'
        name_pattern = r'(\b[A-Z]\.\s+[A-Z][a-z]+)'
        email_pattern = r'email:\s*([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})'
        
        for line in csvreader:
            text = line[1]  # Assuming the relevant text is in the second column
            
            # Find the email, name, university, and specialties in the string using regex
            email_match = re.search(email_pattern, text)
            university_match = re.search(university_pattern, text, flags=re.IGNORECASE)
            specialty_match = re.search(specialty_pattern, text, flags=re.IGNORECASE)
            name_match = re.search(name_pattern, text)
            
            if email_match and name_match and university_match and specialty_match:
                email = email_match.group(1)
                name = name_match.group(1)
                last_name = name.split()[-1]
                
                # Check for duplicates
                if [last_name, email] in final_data:
                    num_duplicate += 1
                else:
                    num_true_data += 1
                    final_data.append([last_name, email])
            else:
                num_false_data += 1
        
        print(f"Number of valid data entries: {num_true_data}")
        print(f"Number of duplicate entries: {num_duplicate}")
        print(f"Number of invalid data entries: {num_false_data}")
        
        return final_data

# Function to write the data to a CSV file
def write_to_csv(data, output_filename):
    with open(output_filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        # Write the header
        csvwriter.writerow(['Last Name', 'Email'])
        # Write the data rows
        csvwriter.writerows(data)

# Main function to execute the program
def main():
    # Prompt the user for the input filename, university name, and specialties
    input_filename = input("Please enter the name of the input file (e.g., input.csv): ")
    output_filename = '/Users/compumagic/Downloads/scopus.output(2).csv'  # Default name for the output CSV file

    university_name = input("Enter the university name to search for: ").title()
    specialty1 = input("Enter the first specialty to search for: ")
    specialty2 = input("Enter the second specialty to search for: ")

    # Read the data from the input file based on university name and specialties
    data = read_input_file(input_filename, university_name, specialty1, specialty2)

    # Write the data to the output CSV file
    write_to_csv(data, output_filename)

    print(f'Data has been successfully written to {output_filename}')

# Execute the main function
if __name__ == '__main__':
    main()
