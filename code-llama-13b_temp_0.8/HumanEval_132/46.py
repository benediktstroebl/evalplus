
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
    return ('[' not in string) == (']' not in string) == False
    
    # return ('[' in string) and (']' in string) and (string.count('[') == string.count(']'))
    
    # count = 0
    # for c in string:
    #     if c == '[':
    #         count += 1
    #     elif c == ']':
    #         count -= 1
    #     if count < 0:
    #         return False
    # return count > 0
    
    # return (string.count('[') != string.count(']')) or (string.count('[') + string.count(']') % 2 != 0)
    
