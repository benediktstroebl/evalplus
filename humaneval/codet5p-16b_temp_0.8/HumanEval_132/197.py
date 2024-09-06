
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

    
    bracket = list(string)
    if bracket[0]!= '[' or bracket[-1]!= ']': return False
    if len(bracket) <= 1: return False
    else:
        for i in range(1, len(bracket)-1):
            if ']' in bracket[i]: return False
    return True
    
