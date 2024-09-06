
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
    def sub_bracket(string, l, r):
        if string[l] == ']' and string[r] == '[':
            return True
        if string[l] == '[' and string[r] == ']':
            return True
        else:
            return False

    if string[0] == ']' or string[-1] == '[' or string.count('[') - string.count(']') != 1:
        return False
    l = 0
    r = len(string) - 1
    while l < r:
        if string[l] == '[' and string[r] == ']':
            if sub_bracket(string, l+1, r-1):
                return True
        elif string[l] == '[' and string[r] == '}':
            return False
        elif string[l] == '{' and string[r] == '}':
            return False
        l += 1
        r -= 1

    return False


