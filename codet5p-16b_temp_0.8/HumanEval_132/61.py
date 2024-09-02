
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

    l = len(string)
    if l % 2 == 0:
        return False
    for i in range(l):
        if string[i] == '[':
            if string[i+1] == ']':
                return False
            elif string[i+1] == '[' and i == 0:
                return False
            else:
                continue
        else:
            continue
    return True

