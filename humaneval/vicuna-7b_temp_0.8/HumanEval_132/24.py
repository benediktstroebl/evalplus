
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
    nesting = 0
    start = 0
    for i in range(len(string)):
        if string[i:i+2] == '[]':
            nesting += 1
        elif string[i:i+1] == ']':
            nesting -= 1
        if nesting > 0:
            start = i
    return start > 0
