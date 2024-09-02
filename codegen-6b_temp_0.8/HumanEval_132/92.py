
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
    if not string:
        return False
    stack = []
    for s in string:
        if s == '[':
            stack.append(s)
        elif s == ']':
            if not stack:
                return False
            if stack[-1] == '[':
                stack.pop()
            else:
                stack.append(s)
    return not stack

