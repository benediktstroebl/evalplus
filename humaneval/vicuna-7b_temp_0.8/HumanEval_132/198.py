
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
    # Create a 2D list to keep track of the current nesting level
    nesting_level = [[0] * 5 for _ in range(5)]

    # Initialize the current index to 0
    current_index = 0

    # Iterate over the characters of the input string
    for char in string:
        # If the current character is a bracket, update the nesting level for that bracket
        if char == '[' or char == ']':
            nesting_level[current_index][0] += 1

        # If the current character is a different bracket, start or end the nested bracket sequence
        elif char == '[' or char == ']':
            if current_index - 1 >= 0:
                # If the nested bracket sequence ends with a different bracket, add one more
                # level to the nesting level for the previous bracket
                nesting_level[current_index - 1][0] += 1
            if current_index + 1 < len(nesting_level):
                # If the nested bracket sequence starts with a different bracket, add one more
                # level to the nesting level for the next bracket
                nesting_level[current_index + 1][0] += 1

        # If the current character is not a bracket, move to the next character
        else:
            current_index += 1

    # Return True if there is at least one nested bracket subsequence, otherwise return False
    return nesting_level[0][0] > 0