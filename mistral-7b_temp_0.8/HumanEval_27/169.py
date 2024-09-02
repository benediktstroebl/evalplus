

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    # YOUR CODE HERE
    new_string = ''
    for i in string:
        if i.islower():
            new_string += i.upper()
        elif i.isupper():
            new_string += i.lower()
    return new_string

