
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
    def helper(string, i, j):
        if i == j:
            return True
        elif string[i] == '[' and string[j] == '[' and string[i-1] == ']' and string[j-1] == ']':
            return True
        elif string[i] == ']' and string[j] == ']':
            return True
        return False

    if helper(string, 0, len(string)-1):
        return True
    else:
        return False
