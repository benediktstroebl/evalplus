

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    lst = list(string)
    for i in range(len(lst)):
        if lst[i].isupper():
            lst[i] = lst[i].lower()
        elif lst[i].islower():
            lst[i] = lst[i].upper()
    return ''.join(lst)
