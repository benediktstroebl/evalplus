
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

    if string[0] == '[' and string[-1] == ']':
        if len(string) == 2:
            return True
        if string[1] == '[' and string[-2] == ']':
            return is_nested(string[2:-2])
        elif string[1] == ']' and string[-2] == '[':
            return is_nested(string[2:-2])
        else:
            return False
    else:
        return False


