import random

# Constants including file names and max lines
MAX_LINES = 4000
FIRST_NAMES_FILE = 'firstNames.txt'
LAST_NAMES_FILE = 'lastNames.txt'
FULL_NAMES_FILE = 'FullNames.txt'

# Function to read and trim the firstNames file
def trim_file_first(firstNames, max_lines):
    
    with open(firstNames, 'r') as file:
        
        lines = file.readlines()
        num_lines = len(lines)

        lines = lines[:max_lines]
        with open(firstNames, 'w') as trimmed_file:
            
            trimmed_file.writelines(lines)
            print(f"{firstNames} trimmed to {max_lines} lines.")

    return num_lines

# Function to read and trim the lastNames file
def trim_file_last(lastNames, max_lines):
    
    with open(lastNames, 'r') as file:
        
        lines = file.readlines()
        num_lines = len(lines)

        lines = lines[:max_lines]
        with open(lastNames, 'w') as trimmed_file:
            
            trimmed_file.writelines(lines)
            print(f"{lastNames} trimmed to {max_lines} lines.")

    return num_lines

# Function to generate full names
def generate_full_names(first_names_file, last_names_file, max_lines):
    
    with open(first_names_file, 'r') as first_file, open(last_names_file, 'r') as last_file:
        
        first_names = [name.strip() for name in first_file.readlines()]
        
        last_names = [name.strip() for name in last_file.readlines()]
        
    full_names = [f"{random.choice(first_names)} {random.choice(last_names)}" for _ in range(max_lines)]
    
    return full_names

# Function to save generated full names to FullNames.txt
def save_full_names(full_names, fullNames):
    
    with open(fullNames, 'w') as random_fullnames_file:
        random_fullnames_file.write('\n'.join(full_names))

# Function to find the longest FullName
def longest_name(full_names):
    
    # Open the file to check
    with open(full_names, 'r') as file:
        full_names = [name.strip() for name in file.readlines()]

    longest_name = max(full_names, key=len)
   
    return longest_name


# Trim firstNames.txt file to 4000(max lines)
num_lines_first_names = trim_file_first(FIRST_NAMES_FILE, MAX_LINES)

# Trim lastNames.txt file to 4000(max lines)
num_lines_last_names = trim_file_last(LAST_NAMES_FILE, MAX_LINES)

# Generate full names
generated_full_names = generate_full_names(FIRST_NAMES_FILE, LAST_NAMES_FILE, MAX_LINES)

# Save generated full names to FullNames.txt
save_into_full_names_file = save_full_names(generated_full_names, FULL_NAMES_FILE)

# Find the longest full name from FullNames.txt
longest_name_result = longest_name(FULL_NAMES_FILE)

# Space for between triming and outputing
print()

# Output number of lines in each file
print(f"Number of lines in {FIRST_NAMES_FILE}: {num_lines_first_names}")
print(f"Number of lines in {LAST_NAMES_FILE}: {num_lines_last_names}")
# Output fullNames genearated
print(f"Full names generated and saved to {FULL_NAMES_FILE}")

print("Longest Name: ", longest_name_result)
