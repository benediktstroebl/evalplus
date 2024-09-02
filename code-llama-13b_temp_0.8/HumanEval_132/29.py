
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
    # Your code here
    
    stack = []
    open_bracket = 0
    closed_bracket = 0
    
    for i in string:
        if i == '[':
            open_bracket = open_bracket + 1
        else:
            closed_bracket = closed_bracket + 1
        
        if closed_bracket > open_bracket:
            return False
        elif closed_bracket == open_bracket:
            return False
        elif closed_bracket < open_bracket:
            return True
        
