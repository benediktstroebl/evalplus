

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    result = list(string)
    for i in range(len(result)):
        if result[i].isupper():
            result[i] = result[i].lower()
        elif result[i].islower():
            result[i] = result[i].upper()
    return "".join(result)

