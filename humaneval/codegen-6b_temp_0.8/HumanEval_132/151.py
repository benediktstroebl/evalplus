
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
    def is_nested_helper(string, left, right, current):
        if left >= right:
            return True
        
        elif string[left] == ']' and current == '[':
            return is_nested_helper(string, left+1, right, ']')
        
        elif string[left] == '}' and current == '{':
            return is_nested_helper(string, left+1, right, '}')
        
        else:
            return False
    
    return is_nested_helper(string, 0, len(string), None)
                
                
        


