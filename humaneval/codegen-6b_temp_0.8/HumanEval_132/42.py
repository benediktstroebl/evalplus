
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
    bracket_stack = []
    for b in string:
        if b == '(':
            bracket_stack.append('(')
        elif b == '[':
            bracket_stack.append('[')
    
    for b in bracket_stack:
        if b == '(':
            if bracket_stack.pop() != '(':
                return False
        elif b == '[':
            if bracket_stack.pop() != '[':
                return False
    
    return True if len(bracket_stack) == 0 else False

