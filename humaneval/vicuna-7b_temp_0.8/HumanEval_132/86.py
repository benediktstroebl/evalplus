
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
    stack = []
    nested = False
    for c in string:
        if c == '[':
            stack.append(c)
            nested = True
        elif c == ']':
            if nested:
                nested = False
                stack.pop()
            else:
                return False
        else:
            if nested:
                nested = False
                stack.append(c)
    return True
