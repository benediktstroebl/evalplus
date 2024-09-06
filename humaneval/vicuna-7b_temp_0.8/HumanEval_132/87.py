
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
    length = len(string)
    for i in range(length):
        if string[i] == '[' and i < length - 2 and string[i+1] == '[' and string[i+2] == ']':
            nesting += 1
        elif string[i] == ']' and i > 0 and string[i-1] == '[' and string[i-2] == ']':
            nesting -= 1
        elif string[i] == '[':
            nesting = 1
    return nesting > 0
