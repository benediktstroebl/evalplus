
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
    s = string.split('[')
    e = string.split(']')
    return True if len(s) != len(e) else False

    # ALTERNATIVE
    #
    # brackets = '['
    # count = 0
    # for char in string:
    #     if char == brackets:
    #         count += 1
    #     elif char == ']':
    #         count -= 1
    #     if count < 0:
    #         return True
    # return False

    # ALTERNATIVE 2
    #
    # s = string.split('[')
    # e = string.split(']')
    # return len(s) != len(e)
