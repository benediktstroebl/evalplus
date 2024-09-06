
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
    # solution 1:
    return '[' in string and ']' in string
    # solution 2:
    #return string.count('[') != string.count(']')
    
    # solution 3:
    # return '[' in string and ']' in string and '[' in string.split(']')
    
    
    '''
    # alternative Way
    cnt = 0
    for char in string:
        if char == '[':
            cnt += 1
        elif char == ']':
            cnt -= 1
        if cnt < 0:
            return False
    return True if cnt == 0 else False
    '''
    
