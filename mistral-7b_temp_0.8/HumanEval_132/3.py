
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

    return True

    # 1st try
    if string == "":
        return False
    if string.count('[') == 0 or string.count(']') == 0:
        return False
    string = string.replace("[]", "")
    if string.count(']') > string.count('['):
        return False
    elif string.count('[') > string.count(']'):
        return False
    else:
        return True

    # 2nd try
    return string.count('[') > 0 and string.count(']') > 0 and string.count('[') < string.count(']')




