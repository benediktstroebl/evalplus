
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

    # check if the string is empty
    if not string:
        return False

    # initialize a variable to store the starting bracket index
    start_index = 0

    # check if the first character is a square bracket
    if string[0] == '[':
        start_index = 1
    else:
        return False

    # check if the last character is a square bracket
    if string[-1] == ']':
        return True

    # check if there is a nested bracket in the string
    for i in range(1, len(string)):
        # check if the current character is a square bracket
        if string[i] == '[':
            # check if the previous character is a square bracket
            if start_index == 0 or (start_index == 1 and string[start_index-1] != ']'):
                # check if the nested bracket is nested within another bracket
                if i - 1 >= 0 and string[i-1] == '[':
                    start_index = i
                    continue

            # if the previous character is not a square bracket, the current character will be the starting bracket index
            start_index = i + 1
        # if the current character is not a square bracket, check if it is a nested bracket
        elif string[i] == ']':
            return True

        # check if the current character is not a square bracket and not a nested bracket
        else:
            return False

    return False
