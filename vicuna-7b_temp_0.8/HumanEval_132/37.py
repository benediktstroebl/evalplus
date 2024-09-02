
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
    current_index = 0
    nested = False
    for i in range(len(string)):
        if string[i] == '[' and string[i+1] == '[' and i < len(string)-2 and string[i+2] == ']':
            nested = True
        elif string[i] == '[' and i < len(string)-1 and string[i+1] == ']':
            nested = False
        elif string[i] == ']' and i < len(string)-1 and nested and string[i+1] == ']':
            nested = False
        if nested:
            current_index = i+2
    return True if current_index < len(string) else False
