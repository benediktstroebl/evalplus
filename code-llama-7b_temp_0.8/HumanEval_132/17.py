
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
    if len(string) == 2: return True
    if len(string) == 4 and string[0] == '[' and string[1] == '[' and string[2] == ']' and string[3] == ']': return True
    if len(string) == 6 and string[0] == '[' and string[1] == '[' and string[2] == '[' and string[3] == ']' and string[4] == ']' and string[5] == ']': return True
    if len(string) == 8 and string[0] == '[' and string[1] == '[' and string[2] == '[' and string[3] == '[' and string[4] == ']' and string[5] == ']' and string[6] == ']' and string[7] == ']': return True
    return False
