
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
    # code goes here

    open_brackets, close_brackets = 0, 0
    nested = False
    
    for i in string:
        if i == '[':
            open_brackets += 1
        else:
            close_brackets += 1
            if close_brackets > open_brackets:
                nested = True
    if open_brackets == close_brackets:
        return True
    elif nested:
        return True
    else:
        return False


