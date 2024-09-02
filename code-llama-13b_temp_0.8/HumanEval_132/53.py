
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
    # Start with False
    # If you find a '[', check for a ']'
    # If you find a ']', check for a '['
    # If either of the above checks are True, return True
    # If you get to the end of the string, return False
    # Return a bool
    a = False
    b = False
    for char in string:
        if char == '[':
            if b:
                return True
        if char == ']':
            if a:
                return True
        if char == '[':
            a = True
        if char == ']':
            a = False
    return False

