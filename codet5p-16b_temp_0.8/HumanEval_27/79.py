

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """

    lst = []
    for char in string:
        if char.islower():
            lst.append(char.upper())
        else:
            lst.append(char.lower())
    return "".join(lst)
    

