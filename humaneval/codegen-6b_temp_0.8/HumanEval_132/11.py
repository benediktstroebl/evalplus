
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
    opened = 0
    closed = 0
    open_brace = 0
    cnt = 0
    for char in string:
        cnt += 1
        if char == '[':
            opened += 1
            open_brace += 1
        if char == ']':
            closed += 1
        if opened == closed:
            return True
    return False
