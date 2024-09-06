

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    new_string = ''
    for char in string:
        if char.isupper():
            new_string += char.lower()
        else:
            new_string += char.upper()
    return new_string

    # You can also use the built-in str.swapcase() method to flip case, or use list
    # comprehension to flip characters:
    # return ''.join(c.upper() if c.islower() else c.lower() for c in string)

