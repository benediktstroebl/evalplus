
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
    def is_nested_aux(s, left, last, right):
        if not s:
            return True
        if s[0] == left:
            return is_nested_aux(s[1:], left, last, right)
        if s[0] == right:
            return is_nested_aux(s[1:], left, last, right)
        return False
    return is_nested_aux(string, '[', ']', ']')

import pytest