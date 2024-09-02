
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
    loops = 0
    if len(string) == 0:
        return False
    for c in string:
        if c == ']':
            loops += 1
        elif c == '[':
            if loops == 0:
                return False
            else:
                loops -= 1
    if loops == 0:
        return True
    else:
        return False

