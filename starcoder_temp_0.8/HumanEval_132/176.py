
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
    i = 0
    d = 0
    for x in string:
        if x == '[':
            i += 1
            d += 1
        if x == ']':
            if i >= 1:
                d -= 1
                i -= 1
    if d == 0:
        return True
    else:
        return False

