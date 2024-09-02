

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    l = list(string)
    for i in range(len(l)):
        if l[i] != l[i].upper():
            l[i] = l[i].upper()
        else:
            l[i] = l[i].lower()
    return "".join(l)

