
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
    # looking at first bracket, if its a list, its nested
    if string[0] == '[' and string[-1] == ']':
        return True
    # if its not a list, keep checking
    else:
        # if its one letter, its not a list
        if len(string) == 1:
            return False
        # look at previous letter and see if there is a list or not
        elif string[-2] == '[' and string[-1] == ']':
            return is_nested(string[:-1])
        else:
            return False