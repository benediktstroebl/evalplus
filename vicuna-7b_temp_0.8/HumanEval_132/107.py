
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
    string = string.upper()
    nested = False
    for i in range(len(string)):
        if string[i] == '[' and i+1 < len(string) and string[i+1] == '[':
            nested = True
            continue
        if string[i] == ']' and i-1 >= 0 and string[i-1] == '[':
            nested = False
            break
        if nested:
            break
    return nested
