
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
    # Initialize variables
    count = 0
    is_nested = False

    # Check if string contains any square brackets
    if '[' in string and ']' in string:
        for char in string:

            # Count the number of open and closed brackets
            if char == '[':
                count += 1
            if char == ']':
                count -= 1
            if count < 0:
                is_nested = True

    return is_nested
