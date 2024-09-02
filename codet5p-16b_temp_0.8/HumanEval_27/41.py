

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """

    if len(string) == 0:
        return string

    result = list(string)

    for idx in range(len(string)):
        if string[idx].islower():
            result[idx] = string[idx].upper()
        elif string[idx].isupper():
            result[idx] = string[idx].lower()

    return "".join(result)
