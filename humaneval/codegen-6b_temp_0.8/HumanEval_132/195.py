
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
    if len(string) < 2:
        return False
    c = 1
    for i in range(1, len(string)):
        if string[i] == '[':
            c += 1
        else:
            c -= 1
        if c < 0:
            return False
    return c > 0

from Test import Test

Test.assertTrue(is_nested('[[]]'), 'Failed to pass a true example')
Test.assertFalse(is_nested('[]]]]]]]]]]]]]'), 'Failed to pass a false example')
Test.assertFalse(is_nested('[]]'), 'Failed to pass a false example')
Test.assertFalse(is_nested('[]'), 'Failed to pass a false example')
Test.assertTrue(is_nested('[[][]]'), 'Failed to pass a true example')
Test.assertTrue(is_nested('[[][]]'), 'Failed to pass a true example')
Test.assertFalse(is_nested('[]]'), 'Failed to pass a false example')
Test.assertFalse(is_nested('[[[]')