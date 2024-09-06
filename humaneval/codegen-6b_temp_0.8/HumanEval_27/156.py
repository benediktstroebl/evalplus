

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    response = ""
    for letter in string:
        if letter.isupper() == True:
            response += letter.lower()
        elif letter.islower() == True:
            response += letter.upper()
        else:
            response += letter

    return response
