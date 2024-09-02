
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
    if string.count('[') == string.count(']') and string.count('[') == 0:
        return False
    elif string.count('[') == string.count(']') and string.count('[') > 0:
        for i in range(len(string)):
            if string[i] == '[':
                x = i
            elif string[i] == ']':
                y = i
                if x+1 < y:
                    return True
                elif x+1 == y:
                    return False
                else:
                    return True
    else:
        return False

