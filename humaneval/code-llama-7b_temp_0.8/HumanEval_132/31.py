
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
    # Opening and closing brackets
    open, close = 0, 0
    # Opening bracket
    for i in range(len(string)):
        if string[i] == "[":
            open += 1
        # Closing bracket
        if string[i] == "]":
            close += 1
        # If we have more closing brackets than opening brackets
        if close > open:
            return True
    return False

