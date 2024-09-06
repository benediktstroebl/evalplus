
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
    for bracket in [item for item in string if item == '[' or item == ']']:
        if bracket == ']' and string.count('[') == string.count(']'):
            return False
        elif bracket == '[' and string.count('[') == string.count(']'):
            return False
            
    if string.count('[') != string.count(']'):
        return False
    else:
        return True

