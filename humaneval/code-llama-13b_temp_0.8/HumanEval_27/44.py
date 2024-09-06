

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    output_string = ""
    for s in string:
        if s.isupper():
            output_string += s.lower()
        elif s.islower():
            output_string += s.upper()
        else:
            output_string += s
    return output_string

