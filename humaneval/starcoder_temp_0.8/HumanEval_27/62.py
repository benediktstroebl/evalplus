

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """

    new_string = []

    for i in range(len(string)):
        char = string[i]
        if char.islower():
            new_string.append(char.upper())
        else:
            new_string.append(char.lower())

    return "".join(new_string)
