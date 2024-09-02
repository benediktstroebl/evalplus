
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

    # check for opening brackets
    open_brackets = 0

    for i in string:
        if i == "[":
            open_brackets += 1

    # check for closing brackets
    close_brackets = 0

    for i in string:
        if i == "]":
            close_brackets += 1

    # return true if nested
    if open_brackets > close_brackets:
        return True
    else:
        return False

