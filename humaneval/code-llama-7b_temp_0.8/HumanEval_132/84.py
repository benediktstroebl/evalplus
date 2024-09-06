
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

    level = 0
    nested = False
    for i in range(len(string)):
        if string[i] == "[" and not nested:
            level += 1
            nested = True
        elif string[i] == "]":
            if level == 0:
                return False
            level -= 1
    return nested
