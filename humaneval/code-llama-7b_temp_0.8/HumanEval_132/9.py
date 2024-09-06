
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
    count, open, close = 0, 0, 0
    for i in string:
        if i == '[':
            if count == 0:
                open = 1
            count += 1
        if i == ']':
            count -= 1
            if count == 0:
                close = 1
    
    return open * close == 0 and count == 0

