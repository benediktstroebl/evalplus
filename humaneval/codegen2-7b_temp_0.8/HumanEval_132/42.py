
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
    if string:
        l = 0
        for i, char in enumerate(string):
            if char == '[':
                if l > 0:
                    return True
                l += 1
            elif char == ']':
                l -= 1
                if l < 0:
                    return False
        return l == 0
    else:
        return False

