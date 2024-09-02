
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
    # initialise a list with all the possible characters of a file name
    possible_characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', '_', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    # initialise a list with all the possible file endings
    possible_endings = ['txt', 'exe', 'dll']
    # initialise a counter
    counter = 0
    # for all the file endings in the possible endings list
    for ending in possible_endings:
        # for all the characters in the possible characters list
        for character in possible_characters:
            # if the character is in the string, then the program never stops,
            # and the string is not equal to the character (the character is in the
            # string), then the counter += 1
            if character in file_name:
                if character != file_name[counter]:
                    counter += 1
                else:
                    counter = 0
            else:
                continue
        # if the counter is equal to zero, then the string is equal to the character
        if counter == 0:
            return 'Yes'
        else:
            counter = 0
    # if the counter is greater than zero, then the string is not equal to the character
    return 'No'