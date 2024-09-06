

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    def split_map(s):
        """ Split a string into a list of substrings and map each substring to its uppercase equivalent. """
        return [s.upper() if s.isupper() else s for s in s.split()]
    
    return ''.join(split_map(string))
