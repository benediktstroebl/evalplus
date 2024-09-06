
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
    if string.count('[') == 0 or string.count(']') == 0:
        return False
    list_ = string.split('[')
    count = 0
    for i in list_:
        if i.count(']') > i.count('['):
            count += 1
        else:
            return False
    return count % 2 == 1
