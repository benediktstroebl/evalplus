
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
    open_counter = 0
    nested = False
    for i in range(0, len(string)):
        if string[i] == '[':
            if open_counter > 0:
                nested = True
            open_counter += 1
        else:
            if open_counter > 0:
                nested = True
            open_counter -= 1
    
    return nested

