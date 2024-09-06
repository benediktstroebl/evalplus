
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
    # test.assert_equals(is_nested('[[]]'), True)
    # test.assert_equals(is_nested('[]]]]]]][[[[[]'), False)
    # test.assert_equals(is_nested('[][]'), False)
    # test.assert_equals(is_nested('[]'), False)
    # test.assert_equals(is_nested('[[][]]'), True)
    # test.assert_equals(is_nested('[[]][['), True)

    # iterate over the string, comparing indices to find the last left and first right brackets
    # to check for nesting, do left_bracket_idx < right_bracket_idx
    left_bracket_idx = []
    right_bracket_idx = []
    for i, char in enumerate(string):
        if char == '[':
            left_bracket_idx.append(i)
        else:
            right_bracket_idx.append(i)
    # return True if there is a valid subsequence where at least one bracket is nested
    return any(left < right for left in left_bracket_idx for right in right_bracket_idx)

