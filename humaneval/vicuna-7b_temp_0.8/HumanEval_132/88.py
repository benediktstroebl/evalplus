
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
    def dfs(s, i, l, r):
        if i == len(s) or s[i] != '[' or s[i] == l or s[i] == r:
            return True
        if s[i] == '[' and s[i+1] != ']':
            dfs(s, i+1, l, r)
            dfs(s, i+2, l, r)
        if s[i] == ']':
            dfs(s, i+1, l+1, r)
            dfs(s, i+2, l+1, r)
        return False
        
    return dfs('', 0, 0, len(string))
