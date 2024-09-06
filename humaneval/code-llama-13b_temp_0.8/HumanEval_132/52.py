
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
    if len(string) == 2:
        return string == '[]'

    return_bool = False
    stack = []
    for i in string:
        if i == '[':
            stack.append('[')
        if i == ']':
            if len(stack) == 0:
                return False
            elif len(stack) > 0:
                stack.pop()
    if len(stack) == 0:
        return_bool = True
    return return_bool

