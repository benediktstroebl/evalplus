
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

    opening = set('[{(')
    closing = set(']})')

    stack = []

    for s in string:
        if s in opening:
            stack.append(s)
        elif s in closing:
            if not stack or stack.pop()!= opening[closing.index(s)]:
                return False

    return not stack

