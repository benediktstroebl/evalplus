
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

    
    if string == '':
        return False
    
    bracket_stack = []
    
    for bracket in string:
        if bracket == '[':
            bracket_stack.append('[')
        elif bracket == ']':
            if bracket_stack[-1] == '[' and bracket_stack[-2] == '[':
                bracket_stack.pop()
                bracket_stack.pop()
            else:
                bracket_stack.append(']')
    return len(bracket_stack) == 0
    
    
    
    
