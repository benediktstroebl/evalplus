
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

    if n % 2 != 0:
        return False

    bal = 0
    for i in range(n):
        if string[i] == '[':
            bal += 1
        elif string[i] == ']':
            if bal < 1:
                return False
            else:
                bal -= 1

    return True if bal == 0 else False
    
