
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
    for c in string:
        if c == '[':
            stack.append(c)
        elif c == ']':
            if stack:
                if stack[-1] == '[' and stack[-2] == ']':
                    stack.pop()
                    stack.pop()
                else:
                    return False
                stack.pop()
        else:
            stack.pop()
    return not stack