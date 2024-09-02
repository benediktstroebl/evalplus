

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    # Solution 1:
    # return ''.join(char.lower() if char.isupper() else char.upper() for char in string)

    # Solution 2:
    # result = []
    # for char in string:
    #     if char.islower():
    #         result.append(char.upper())
    #     else:
    #         result.append(char.lower())
    # return ''.join(result)

    # Solution 3:
    return ''.join(map(lambda char: char.lower() if char.isupper() else char.upper(), string))

