

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    uppercase = set()
    lowercase = set()
    
    for char in string:
        if char.isupper():
            uppercase.add(char)
        else:
            lowercase.add(char)
    
    return ''.join([uppercase if char.isupper() else lowercase.pop() for char in string])