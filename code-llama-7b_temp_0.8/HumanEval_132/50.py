
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
    if string.count('[]') == 0: return False
    if string.count('[]') == 1: return True
    result = False
    stack = []
    for char in string:
        if char == '[':
            stack.append(char)
        if char == ']':
            if not stack:
                return False
            stack.pop()
            if not stack:
                result = True
    return result
    
