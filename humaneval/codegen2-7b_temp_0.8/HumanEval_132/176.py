
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
    for i in string:
        if i in '[':
            stack.append(i)
        elif i in ']':
            if not stack:
                return False
            if stack[-1] == '[':
                stack.pop()
            elif stack[-1] == ']':
                stack.pop()
                stack.pop()
            else:
                return False
    return not stack
