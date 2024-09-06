
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
    index = 0
    nested = False
    while index < len(string) - 1:
        if string[index] == '[' and string[index+1] == '[' and string[index+2] == '[':
            nested = True
            index += 2
        elif string[index] == ']' and string[index+1] == ']' and string[index+2] == ']':
            nested = False
            index += 2
        elif nested:
            if string[index] == '[' and string[index+1] == ']':
                nested = False
            elif string[index] == ']' and string[index+1] == '[':
                nested = True
        index += 1
    return nested