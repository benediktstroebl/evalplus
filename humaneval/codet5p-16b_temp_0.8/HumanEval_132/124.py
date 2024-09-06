
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

    def is_nested_subsequence(s, start=0):
        if len(s) <= 1: return True
        elif s[start] == '[':
            return is_nested_subsequence(s[start+1:], start+1)
        elif s[start] == ']':
            return is_nested_subsequence(s[:start], start+1)
        return False

    return is_nested_subsequence(string)
