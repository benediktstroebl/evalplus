

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    # new_string = string[::-1]
    # for char in string:
    #     if char.isupper():
    #         new_string = new_string.replace(char, char.lower())
    #     else:
    #         new_string = new_string.replace(char, char.upper())
    # return new_string
    new_string = ''
    for char in string:
        if char.islower():
            new_string += char.upper()
        else:
            new_string += char.lower()
    return new_string

