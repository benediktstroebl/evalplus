
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

    n = len(string)
    if n == 0:
        return False

    if n % 2 == 1:
        return False

    if n == 2:
        return True

    l_count = 0
    r_count = 0
    for i in range(n):
        if string[i] == '[':
            l_count += 1
        if string[i] == ']':
            r_count += 1

    if l_count == r_count:
        return True
    else:
        return False

