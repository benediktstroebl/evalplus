def is_nested(string):
    '''
    Check if the given string contains a valid nested bracket subsequence.
    Return True if a string contains '[[]]' or '[][]'.
    '''
    return ('[]]' in string or '[][]' in string)