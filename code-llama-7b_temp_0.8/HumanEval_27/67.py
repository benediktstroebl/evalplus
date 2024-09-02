

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """

    # Use a loop to iterate through each character in the string
    new_string = ''
    for char in string:
        # if character is uppercase, convert it to lowercase and vice versa
        if char.isupper():
            new_string += char.lower()
        else:
            new_string += char.upper()
    return new_string
