
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
    s = list(string)
    c = s.count('[')
    if c == 0:
        return False
    elif c % 2 == 0:
        return False
    else:
        (s.remove('[') if s[-1] == '[' else s.pop()).remove('[')
        return c != s.count('[')
