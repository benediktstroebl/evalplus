

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    # Get a list of characters
    string_list = list(string)
    # Flip the case for each character
    for i in range(len(string_list)):
        if string_list[i].islower():
            string_list[i] = string_list[i].upper()
        elif string_list[i].isupper():
            string_list[i] = string_list[i].lower()
    # Join the list back into a string
    new_string = "".join(string_list)
    return new_string

