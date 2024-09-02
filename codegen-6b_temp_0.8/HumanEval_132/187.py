
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
    n = len(string)
    if n < 1:
        return False
    if n == 1:
        return False
    if string[0] != '[' or string[-1] != ']':
        return False
    stack = []
    for i, c in enumerate(string):
        if c == '[':
            stack.append(i)
        elif c == ']':
            if not stack:
                return False
            stack.pop()

    return len(stack) == 0
