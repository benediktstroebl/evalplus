
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
    string = string.upper()
    nesting_level = 0
    result = True
    for char in string:
        if char == '[':
            nesting_level += 1
        elif char == ']':
            nesting_level -= 1
            if nesting_level < 0:
                result = False
                break
    return result