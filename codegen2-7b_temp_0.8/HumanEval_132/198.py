
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
    if '[' not in string:
        return False
    
    nested = 0
    stack = []
    for i in string:
        if i == '[':
            stack.append(i)
            nested += 1
        elif i == ']' and len(stack) > 0:
            nested -= 1
            stack.pop()
        elif i == ']' and len(stack) == 0:
            return True
    
    return len(stack) == 0 and nested ==
