
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
    # Check the first character
    if string[0] == '[':
        return True

    # Check the first character
    if string[-1] == ']':
        return True

    # Return False if the string is empty
    if len(string) == 0:
        return False

    # Check if the first character is a square bracket
    if string[0] != '[':
        return False

    # Check if the last character is a square bracket
    if string[-1] != ']':
        return False

    # Check if the first character is a square bracket and the last character is a square bracket
    if string[0] == '[' and string[-1] == ']':
        return True

    # Check if the first character is a square bracket and the last character is a square bracket
    if string[0] == '[' and string[-1] == ']':
        return True

    # Check if the first character is a square bracket and the last character is a square bracket
    if string[0] == '[' and string[-
