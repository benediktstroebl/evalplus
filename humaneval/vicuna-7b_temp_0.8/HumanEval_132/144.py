
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
    def helper(s):
        if not s:
            return False
        for i in range(len(s)):
            if i == 0:
                continue
            if s[i-1] != ']' and s[i-1] != '[':
                return False
            if s[i-1] == '[':
                if s[i] != ']':
                    return False
                if s[i+1] != '[':
                    return False
            if s[i-1] == ']':
                if s[i+1] != ']':
                    return False
        return True
    return helper