
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
    def helper(substring):
        if not substring:
            return True
        for i in range(1, len(substring)):
            if substring[i] == '[' and substring[i-1] == '[' and substring[i+1] == '[':
                return helper(substring[i+2:])
        return False
    return helper(string)
