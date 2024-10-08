
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

    open = 0
    close = 0
    for char in string:
        if char == '[':
            open += 1
            if open > 1:
                return True
        elif char == ']':
            close += 1
            if close > 1:
                return True
        else:
            print('Character is not a square bracket.')
    return False
