
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
    def helper(length, curr, string):
        if length == 0:
            return True
        if length == 1 and curr == ']':
            return True
        if curr == '[' and not helper(length - 1, string[curr+1:], string):
            return False
        if helper(length - 1, curr, string):
            return True
        if curr == ']' and not helper(length - 1, string[curr-1:], string):
            return True
        if helper(length - 1, curr, string):
            return True
        return False
        
    return helper(0, ']', string)