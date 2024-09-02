
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
    if string == '': return False
    i = 0
    lvl = 0
    while i < len(string):
        if string[i] == '[':
            lvl += 1
        else:
            lvl -= 1
        if lvl == 0:
            return False
        i += 1
    return True
