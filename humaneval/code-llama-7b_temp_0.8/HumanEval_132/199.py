
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
    n, c = 0, 0
    for i in range(len(string)):
        if string[i] == ']':
            n -= 1
            if n < 0:
                return False
        elif string[i] == '[':
            n += 1
        if n == c:
            c += 1
    return n == 0
