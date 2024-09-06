

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    output_string = ""
    for char in string:
        if char.isupper():
            output_string += char.lower()
        elif char.islower():
            output_string += char.upper()
        else:
            output_string += char
    return output_string

