

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    def _flip_case(s):
        if not s:
            return s
        if s.islower():
            return s.upper()
        if s.isupper():
            return s.lower()
        return s
    return _flip_case(string)

@app.task
