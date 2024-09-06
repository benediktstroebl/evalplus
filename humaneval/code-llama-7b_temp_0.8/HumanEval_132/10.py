
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
    open = 0
    closed = 0
    for i in string:
        if i == '[':
            open += 1
        elif i == ']':
            closed += 1
    if open == 0 or closed == 0:
        return False
    return True if open - closed == 0 else is_nested(string[:-1])

