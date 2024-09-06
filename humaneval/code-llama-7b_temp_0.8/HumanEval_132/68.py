
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
    l1 = 0
    l2 = 0
    for i in string:
        if i == '[':
            l1 += 1
        elif i == ']':
            l2 += 1
        if l1 > 0 and l2 > 0:
            return True
    if l1 == l2:
        return False
    else:
        return True
