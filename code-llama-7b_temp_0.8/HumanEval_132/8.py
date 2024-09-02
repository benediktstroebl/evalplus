
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
    # Set the open and closed brackets
    open_bracket = '['
    closed_bracket = ']'

    # Get the length of the string
    length = len(string)

    # Init a count of nested open and closed bracket pairs to zero
    count_open = 0
    count_closed = 0

    # Init a nested boolean to False
    nested = False

    # Loop over the string character-by-character
    for i, c in enumerate(string):

        # If the current character is an open bracket, increment the count_open
        if c == open_bracket:
            count_open += 1

        # If the current character is a closed bracket, increment the count_closed
        if c == closed_bracket:
            count_closed += 1

        # If the count_closed is equal to the count_open
        if count_closed == count_open:
            nested = True

        # If the length of the string is evenly divisible by two
        if length % 2 == 0:
            return nested

