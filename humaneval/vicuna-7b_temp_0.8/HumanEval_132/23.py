
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
    for i in range(1, len(string)):
        for j in range(i):
            if string[i] == '[' and string[j] == ']':
                return False
            elif string[i] == ']' and string[j] == '[':
                return True
            elif string[i] == ']' and string[j] == ']':
                return True
        return False

    return True
