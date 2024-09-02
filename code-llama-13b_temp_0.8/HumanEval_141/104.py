
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
    if file_name.count('.') == 1:
        if file_name.startswith('a') or file_name.startswith('A') or file_name.startswith('b') or file_name.startswith('B') or file_name.startswith('c') or file_name.startswith('C') or file_name.startswith('d') or file_name.startswith('D') or file_name.startswith('e') or file_name.startswith('E') or file_name.startswith('f') or file_name.startswith('F') or file_name.startswith('g') or file_name.startswith('G') or file_name.startswith('h') or file_name.startswith('H') or file_name.startswith('i') or file_name.startswith('I') or file_name.startswith('j') or file_name.startswith('J') or file_name.startswith('k') or file_name.startswith('K') or file_name.startswith('l') or file_name.startswith('L') or file_name.startswith('m') or file_name.startswith('M') or file_name.startswith('n') or file_name.startswith('N') or file_name.startswith('o') or file_name.startswith('O') or file_name.startswith('p') or file_name.startswith('P') or file_name.startswith('q') or file_name.startswith('Q') or file_name.startswith('r') or file_name.startswith('R') or file_name.startswith('s') or file_name.startswith('S') or file_name.startswith('t') or file_name.startswith('T') or file_name.startswith('u') or file_name.startswith('U') or file_name.startswith('v') or file_name.startswith('V') or file_name.startswith('w') or file_name.startswith('W') or file_name.startswith('x') or file_name.startswith('X') or file_name.startswith('y') or file_name.startswith
