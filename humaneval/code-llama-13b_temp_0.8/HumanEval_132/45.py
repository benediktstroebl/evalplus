
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
    i = 0
    count = 0
    while i < len(string)-1:
        if string[i] == '[' and string[i+1] == '[':
            count += 1
        elif string[i] == ']' and string[i+1] == ']':
            count += 1
        elif string[i] == ']' and string[i+1] == '[':
            count += 1
        i += 1
    if count >= 2:
        return True
    return False


