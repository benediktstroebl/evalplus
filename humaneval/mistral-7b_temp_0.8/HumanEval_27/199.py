

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    answer = ""
    for c in string:
        if c.isupper():
            answer += c.lower()
        else:
            answer += c.upper()
    return answer



