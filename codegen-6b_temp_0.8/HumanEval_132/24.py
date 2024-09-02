
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
    
    if string[0] != '[':
        return False
    elif len(string) == 1:
        return False
    elif len(string) == 2:
        return True
    
    new = []
    for i, bracket in enumerate(string):
        if not new and bracket == ']':
            return False
        elif bracket == '[':
            new.append(bracket)
        elif bracket == ']':
            if len(new) == 0:
                return False
            elif new[0] == '[':
                new.append(bracket)
            else:
                new.pop()
    return False if new else True


import itertools
