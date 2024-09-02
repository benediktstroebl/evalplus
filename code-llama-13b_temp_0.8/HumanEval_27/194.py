

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """

    string_list = list(string)
    string_list_len = len(string_list)
    for idx, char in enumerate(string_list):
        if char.isalpha():
            if char.isupper():
                string_list[idx] = char.lower()
            elif char.islower():
                string_list[idx] = char.upper()

    return ''.join(string_list)

