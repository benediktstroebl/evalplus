
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
    if len(string) % 2 != 0: return False
    if not "]" in string or not "[" in string: return False
    
    x, y = 0, 0
    for i in string:
        if i == "[":
            x+=1
            y=0
        if i == "]":
            x-=1
            y=1
        if x < 0 and y == 0: return False
    if x == 0 and y == 1: return True
    if x == 0 and y == 0: return False
    return True
