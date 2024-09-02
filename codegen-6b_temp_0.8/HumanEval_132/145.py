
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
    if len(string) == 0:
        return True

    if len(string) > 1 and string[0] == string[-1] == ']':
        return is_nested(string[1:-1])

    if len(string) > 1 and string[0] == string[-1] == ']':
        return is_nested(string[1:])

    return False

