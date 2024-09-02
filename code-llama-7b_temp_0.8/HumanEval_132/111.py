
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
    # Get the length of the string.
    length = len(string)

    # Create a counter of open and close brackets.
    counter = [0] * 2

    # Loop over the length of the string.
    for i in range(length):

        # Check if the string[i] is an open bracket.
        if string[i] == "[":
            counter[0] += 1

        # Check if the string[i] is a close bracket.
        if string[i] == "]":
            # Check if the counter is negative
            if counter[0] < 0:
                return False
            counter[0] -= 1

    # If the counter is 0, then the string is nested.
    if counter[0] == 0:
        return True
    return False
    
