
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
    if len(string) < 2:
        return False
    if string[0] != '[' or string[-1] != ']':
        return False
    balance = 0
    for i, v in enumerate(string[1:-1]):
        if v == '[':
            balance += 1
        elif v == ']':
            balance -= 1
        if balance < 0:
            return False
    if balance == 0:
        return False
    return True
    
