
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
    
    if len(string) == 0:
        return False
    if len(string) == 1:
        return False

    openers = 0
    closers = 0
    brackets = {'(':')', '{':'}', '[':']'}

    for char in string:
        if char in brackets.keys():
            closers += 1
        elif char in brackets.values():
            openers += 1

    return not (openers == 0 and closers == 0)


