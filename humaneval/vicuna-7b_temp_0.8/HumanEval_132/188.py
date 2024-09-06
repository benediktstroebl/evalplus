
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
    string = ''.join(string)
    n = 0
    nested = 0
    for i in range(len(string)):
        if string[i] == '[' and i < len(string) - 1 and string[i + 1] == '[' and nested == 0:
            nested += 1
        elif string[i] == ']' and i < len(string) - 1 and string[i + 1] == ']' and nested > 0:
            nested -= 1
        if nested > 0:
            n += 1
            if i + nested < len(string) and string[i + nested] == '[':
                nested += 1
        if nested == 0:
            break
    return n > 0