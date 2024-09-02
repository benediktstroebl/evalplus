
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
    nesting_level = 0
    for i, c in enumerate(string):
        if c == '[' and nesting_level > 0:
            nesting_level -= 1
        elif c == ']' and nesting_level == 0:
            return True
        elif c == ']':
            nesting_level += 1
    return False