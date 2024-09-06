
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
    def is_single_bracket(s):
        num = 0
        for c in s:
            if c == '[':
                num += 1
            elif c == ']':
                num -= 1
            if num < 0:
                return False
        if num != 0:
            return False
        return True

    def nested(s):
        if not s:
            return False
        if is_single_bracket(s):
            return True
        for i in range(len(s)):
            if s[i] == '[' and is_single_bracket(s[i+1:]):
                return True
        return False

    return nested(string)
