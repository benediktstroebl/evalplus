
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
    string = string.replace('[', '').replace(']', '')
    if len(string) == 0: return True
    elif len(string) % 2 == 0: return False
    elif len(string) == 1: return False
    elif '[' not in string and ']' not in string: return False
    elif '[' not in string: return is_nested(string[1:])
    elif ']' not in string: return is_nested(string[:-1])
    elif string[0] == ']':
        return is_nested(string[:-1])
    else:
        return is_nested(string[1:])















