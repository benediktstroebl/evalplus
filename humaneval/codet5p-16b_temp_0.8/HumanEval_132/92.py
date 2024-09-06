
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

    if string == '[]':
        return False
    
    bracket_stack = []
    for i, char in enumerate(string):
        if char == '[':
            bracket_stack.append(i)
        elif char == ']':
            if bracket_stack and string[bracket_stack[-1]] == '[':
                bracket_stack.pop()
            else:
                bracket_stack.append(i)
                break
            
    return True if not bracket_stack else False

