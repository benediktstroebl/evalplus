
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

    
    index = 0
    nested = False
    
    while index < len(string):
        
        if string[index] == '[':
            nested = True
        
        if string[index] == ']':
            if nested == True:
                nested = False
            else:
                return False
        
        index += 1
    
    return nested

