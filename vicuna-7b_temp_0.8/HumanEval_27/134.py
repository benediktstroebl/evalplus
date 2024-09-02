

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    def flip_case_dict(s):
        return dict(((ord(c) - ord('A') + 26, c) for c in s))
    return ''.join(flip_case_dict(string))
