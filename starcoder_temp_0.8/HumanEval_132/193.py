
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
    start = string.find("[")
    end = string.find("]")
    if start == -1 or end == -1:
        return False
    while start!= -1 and end!= -1:
        string = string[start:end+1]
        start = string.find("[")
        end = string.find("]")
        if start == -1 or end == -1:
            return False
    return True
