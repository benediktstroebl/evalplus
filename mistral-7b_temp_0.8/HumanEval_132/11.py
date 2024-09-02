
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
    check_string = '['
    for char in string:
        if char == check_string:
            check_string = ']'
        elif char == check_string:
            check_string = '['
        else:
            return False
    return True
    '''
    for bracket in string:
        if bracket == '[':
            if is_nested(string[1:]):
                return True
        if bracket == ']':
            return False
    return True
    '''
