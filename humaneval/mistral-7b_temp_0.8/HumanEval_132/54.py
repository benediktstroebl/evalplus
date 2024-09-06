
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
    is_nested = False
    open_brackets = 0
    close_brackets = 0
    for bracket in string:
        if bracket == '[':
            open_brackets += 1
        elif bracket == ']':
            close_brackets += 1
        elif close_brackets == open_brackets:
            is_nested = True
            break
    return is_nested

