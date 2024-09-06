
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
    # Check if the string is empty
    if not string:
        return False

    # Check if the string contains only square brackets
    if '[]' not in string:
        return False

    # Check if the string contains nested brackets
    nest_count = 0
    for char in string:
        if char == '[':
            nest_count += 1
        elif char == ']':
            nest_count -= 1
            if nest_count < 0:
                return False
    if nest_count > 0:
        return True
    return False