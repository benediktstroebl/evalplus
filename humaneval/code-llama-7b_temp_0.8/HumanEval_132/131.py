
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
    # If string is empty or only contains one character, it cannot be nested
    if (string == None or len(string) <= 1):
        return False

    # Get the index of the closing bracket, if one is found,
    # use the index to get the rest of the string
    for i in range(0, len(string)):
        if (string[i] == "]"):
            string = string[i + 1:]
            break

    # If the string is empty, it cannot be nested
    if (len(string) == 0):
        return False

    # Get the index of the opening bracket, if one is found,
    # use the index to get the rest of the string
    for i in range(0, len(string)):
        if (string[i] == "["):
            string = string[i + 1:]
            break

    # If the string is empty, it cannot be nested
    if (len(string) == 0):
        return False

    # Recursively call the function with the remaining string
    return is_nested(string)
