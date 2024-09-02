
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
    # Initialize an empty string to store the length of nested brackets
    nested = 0
    # Iterate over each character in the input string
    for char in string:
        # If the current character is a square bracket,
        # increment the nested counter and check if it is 1
        if char == ']':
            nested += 1
            if nested == 1:
                return True
        # If the current character is not a square bracket,
        # check if the previous character was a square bracket
        if not char == '[':
            if len(string) - nested >= 1:
                return True
    return False