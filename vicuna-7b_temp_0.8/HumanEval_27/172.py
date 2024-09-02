

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    def flip_case_re(match):
        return str(match.group().upper() + match.group().lower())

    return ''.join([flip_case_re(re.search(r'[a-z]', c)) if c.islower() else flip_case_re(re.search(r'[A-Z]', c)) for c in string])
