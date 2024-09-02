
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
    if len(string)%2 == 1:
        return False
    marker = 0
    for i in range(len(string)):
        if string[i] == '[' and marker == 0:
            marker = 1
        if string[i] == ']' and marker == 1:
            marker = 0
        if string[i] == '[' and marker == 0:
            return False
    return True

