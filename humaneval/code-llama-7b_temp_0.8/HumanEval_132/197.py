
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
    open_brackets = '[('
    close_brackets = '])'
    open_counter = 0
    close_counter = 0
    for i in string:
        if i in open_brackets:
            open_counter += 1
        if i in close_brackets:
            close_counter += 1

    return True if (open_counter == close_counter) or (open_counter > close_counter) else False

