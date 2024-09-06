
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
    string = str(string)
    nested = False
    for i in range(len(string)-1):
        if string[i] == '[' and string[i+1] == '[' and string[i+2] == '[':
            nested = True
        elif string[i] == ']' and string[i+1] == ']' and string[i+2] == ']':
            nested = False
        elif nested:
            if string[i] != ']' or string[i+1] != ']':
                nested = False
    return nested
