
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
    if string[0]!= '[' or string[-1]!= ']':
        return False
    nested = 1
    for i in range(1, len(string) - 1):
        if string[i] == '[':
            nested += 1
        elif string[i] == ']':
            nested -= 1
        if nested < 0:
            return False
    return True
