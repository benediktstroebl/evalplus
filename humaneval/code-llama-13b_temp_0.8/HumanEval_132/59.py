
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
    
    if string[0] != '[' or string[-1] != ']':
        return False
    
    nested_count = 0
    unclosed_count = 0
    
    for i in range(len(string)):
        if string[i] == '[':
            unclosed_count += 1
        
        elif string[i] == ']':
            unclosed_count -= 1
            
            if unclosed_count < 0:
                return False
            
            if nested_count == 0:
                nested_count += 1
            else:
                nested_count -= 1
    
    return nested_count > 0
