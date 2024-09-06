
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
    l = len(string)
    if l == 2:
        if string[0]== '[' and string[1] == ']':
            return False
        else:
            return True
    elif l == 0:
        return False
    elif string[0] == '[' and string[-1] == ']':
        return False
    else:
        for index, x in enumerate(string):
            if x == '[':
                if string.index(']') > index and string.index(']') < l-1:
                    return True
                else:
                    return False
    return False
