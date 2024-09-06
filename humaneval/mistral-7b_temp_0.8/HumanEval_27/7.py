

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    new_string = string
    for i, char in enumerate(new_string):
        if char.isupper():
            new_string = new_string[:i] + char.lower() + new_string[i + 1:]
        elif char.islower():
            new_string = new_string[:i] + char.upper() + new_string[i + 1:]
    return new_string

