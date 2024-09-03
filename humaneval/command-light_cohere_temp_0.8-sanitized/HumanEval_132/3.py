def is_nested(string):
    '''
    Check if a string contains only square brackets
    and returns True if it has a valid nested brackets subsequence
    '''
    return all([isinstance(x, '[') and is_nested('[') for x in string.isinstance(']')]) and all([isinstance(x, '[') and is_nested(']') for x in string.isinstance('[')]) and all([isinstance(x, ']') and is_nested(']') for x in string.isinstance(']')])