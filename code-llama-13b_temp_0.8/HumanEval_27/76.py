

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """

    lower_indices = []
    upper_indices = []
    for idx, char in enumerate(string):
        if char.islower():
            lower_indices.append(idx)
        else:
            upper_indices.append(idx)

    for idx in lower_indices:
        string = string[:idx] + string[idx].upper() + string[idx + 1:]
    for idx in upper_indices:
        string = string[:idx] + string[idx].lower() + string[idx + 1:]

    return string

