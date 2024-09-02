
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


    '''
    def is_nested(string):
        if string == '' or string == '[':
            return True
        if string.endswith('['):
            return is_nested(string[:-1])
        if string.endswith(']'):
            return is_nested(string[:-1])

    return is_nested(string)
    '''

    def is_nested(string):
        return string.endswith('[') or is_nested(string[:-1])

    return is_nested(string)


