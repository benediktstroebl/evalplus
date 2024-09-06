
def is_nested(string):
    '''
    Create a function that takes a string as input which contains only square brackets.
    The function should return True if and only if there is a valid subsequence of brackets 
    where at least one bracket in the subsequence is nested.

    is_nested('[[]]') ➞ True
    is_nested('[]]]]]]][[[[[]') ➞ False
    is_nested('[][]') ➞ False
    is_nested('[]') ➞ False
    is_nested('[[][]]') ➞ True
    is_nested('[[]][[') ➞ True
    '''
    if string.count('[') == string.count(']') and string.count('[') == 0:
        return True
    if string.count('[') > string.count(']'):
        if string.startswith(']'):
            return is_nested(string[1:])
        for i, char in enumerate(string):
            if char == '[':
                if is_nested(string[i+1:]):
                    return True
                else:
                    return is_nested(string[i+1:])
    if string.count('[') < string.count(']'):
        if string.endswith('['):
            return is_nested(string[:-1])
        for i, char in enumerate(string):
            if char == ']':
                if is_nested(string[:i]):
                    return True
                else:
                    return is_nested(string[:i])
    else:
        return False
    
