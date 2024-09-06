
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
    maxi = 0
    for i in range(n):
        if string[i] == '[':
            maxi += 1
        if string[i] == ']':
            maxi -= 1
        if maxi < 0:
            return False
    return maxi == 0
