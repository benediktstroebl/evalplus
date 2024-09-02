
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
    ans = []
    for char in string:
        if char == '[' or char == ']' or char == '?':
            ans.append(char)
            if len(ans) > 1 and (ans[-2] == '[' and ans[-1] == ']' or ans[-2] == '?' and ans[-1] == '?'):
                return True
            while len(ans) >= 2 and (ans[-2] == '[' and ans[-1] == ']'):
                ans.pop()
                ans.pop()
    return False
