
def file_name_check(file_name):
    """Create a function which takes a string representing a file's name, and returns
    'Yes' if the the file's name is valid, and returns 'No' otherwise.
    A file's name is considered to be valid if and only if all the following conditions 
    are met:
    - There should not be more than three digits ('0'-'9') in the file's name.
    - The file's name contains exactly one dot '.'
    - The substring before the dot should not be empty, and it starts with a letter from 
    the latin alphapet ('a'-'z' and 'A'-'Z').
    - The substring after the dot should be one of these: ['txt', 'exe', 'dll']
    Examples:
    file_name_check("example.txt") # => 'Yes'
    file_name_check("1example.dll") # => 'No' (the name should start with a latin alphapet letter)
    """

    
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    alphabet = [chr(n) for n in range(ord('a'), ord('z')+1)]
    latin_alphabet = alphabet+[chr(n) for n in range(ord('A'), ord('Z')+1)]
    
    if not all(x in digits for x in file_name):
        return 'No'
    
    if file_name.count('.')!= 1:
        return 'No'
    
    dot_index = file_name.index('.')
    
    if dot_index!= len(file_name)-1:
        if dot_index+1 > len(file_name):
            return 'No'
        if file_name[dot_index+1] in ['txt', 'exe', 'dll']:
            return 'No'
    
    if file_name[:dot_index] == '' or not file_name[:dot_index][0] in lat
