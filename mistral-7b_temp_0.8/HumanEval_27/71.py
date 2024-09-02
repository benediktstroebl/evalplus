

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    # your code here
    output = ''
    for letter in string:
        if letter.islower():
            output += letter.upper()
        else:
            output += letter.lower()
    return output

