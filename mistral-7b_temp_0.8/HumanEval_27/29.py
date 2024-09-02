

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    lower_case_characters = set('abcdefghijklmnopqrstuvwxyz')
    upper_case_characters = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    string_result = []
    for character in string:
        if character in lower_case_characters:
            string_result.append(character.upper())
        elif character in upper_case_characters:
            string_result.append(character.lower())
        else:
            string_result.append(character)
    return ''.join(string_result)

