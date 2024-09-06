
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
    # This solution is a bit easier to understand than the other one, and looks 
    # better because it doesn't use so many variables.
    # However, it's probably not as efficient as the other one.
    stack = 0
    for char in string:
        if char == '[':
            stack += 1
        else:
            stack -= 1
        if stack < 0:
            return False
    return stack > 0
