

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    #TODO: Flip all characters in the string

    #solution
    ans = ''
    for i in string:
        if i.islower():
            ans += i.upper()
        elif i.isupper():
            ans += i.lower()
    return ans

