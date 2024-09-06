
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

    result = True
    bracket_stack = []
    bracket_dict = {']': '[', ')': '('}
    
    if string[0] == '[':
        return False
    
    for bracket in string:
        if bracket == '[':
            bracket_stack.append(bracket)
        elif bracket in bracket_dict:
            if bracket_stack:
                bracket_stack.pop()
            else:
                return False
            
    return True if not bracket_stack else False
