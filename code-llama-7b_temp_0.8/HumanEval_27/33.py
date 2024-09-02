

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    # print(f"string type: {type(string)}")
    # print(f"string: {string}")
    new_string = ""
    for i in range(len(string)):
        if string[i].isupper():
            # print(f"char: {string[i]}")
            new_string += string[i].lower()
        elif string[i].islower():
            # print(f"char: {string[i]}")
            new_string += string[i].upper()
    return new_string
