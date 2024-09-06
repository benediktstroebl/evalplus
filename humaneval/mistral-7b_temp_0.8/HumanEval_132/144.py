
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
    open = []
    close = []
    for i in string:
        if i == '[':
            open.append(i)
        elif i == ']':
            close.append(i)
    if len(open) != len(close):
        return False
    elif len(open) == 0 or len(close) == 0:
        return False
    else:
        return True
