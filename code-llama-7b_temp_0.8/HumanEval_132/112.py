
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
    import re

    if len(string) % 2 == 0:
        return False
    
    for i in re.finditer(r'\[\]', string):
        try:
            if i.group() in string[i.start() + 1: i.end() - 1] and i.group() == '[]':
                return True
        except:
            return False
        
    return False

