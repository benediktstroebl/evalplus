
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
    if len(string) < 2:
        return False
    for i in range(0, len(string) - 1):
        if string[i] == '[' and string[i + 1] == ']':
            return False
        if string[i] == '[' and string[i + 1] != ']':
            for j in range(i + 2, len(string)):
                if string[j] == '[':
                    return True
        if string[i] == ']' and string[i - 1] != '[':
            for j in range(i - 2, -1, -1):
                if string[j] == ']':
                    return True
    return False

