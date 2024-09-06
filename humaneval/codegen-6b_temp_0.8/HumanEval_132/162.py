
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
    b = 0
    c = 0
    for i in string:
        if i == '[' and b == 0:
            b += 1
        elif i == ']' and b == 1:
            b -= 1
        elif i == '[' and b > 1:
            c += 1
    if b == 0 and c == 0:
        return True
    return False
