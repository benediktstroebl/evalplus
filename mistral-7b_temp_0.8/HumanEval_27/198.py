

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    if string == "":
        return ""
    result = ""
    for character in string:
        if character.isupper():
            result += character.lower()
        elif character.islower():
            result += character.upper()
        else:
            result += character
    return result

