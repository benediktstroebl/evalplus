
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
    square_bracket_count = 0
    nested_bracket_count = 0
    for char in string:
        if char == '[':
            square_bracket_count += 1
        else:
            square_bracket_count -= 1
        if char == '[':
            nested_bracket_count += 1
        else:
            nested_bracket_count -= 1
        if square_bracket_count < 0:
            return False
        if square_bracket_count > 0 and nested_bracket_count < 0:
            return True
    return False
