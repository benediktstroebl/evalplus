
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
    # Get the count of opening and closing brackets
    open_brackets = string.count('[')
    close_brackets = string.count(']')
    
    # Compare the counts
    if open_brackets == close_brackets:
        return False
    
    # Add an extra opening bracket
    if open_brackets > close_brackets:
        string += ']'
    
    # Get the count of opening and closing brackets again
    open_brackets = string.count('[')
    close_brackets = string.count(']')
    
    # Compare the counts
    if open_brackets == close_brackets:
        return False
    
    # If you are here, then the string contains a nested bracket.
    return True

