
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
    # Make a set to keep track of the open bracket pairs
    pairs = set()
    # Create a set to keep track of the open bracket pairs
    depth = 0
    # Loop through the string
    for char in string:
        # If the char is a closing bracket
        if char == ']':
            # Set a depth to zero
            depth = 0
            # If the depth is 0 and the current character is '['
            if depth==0:
                # Remove the pair from the set
                pairs.remove('[')
            # If the depth is greater than 0, remove from the set
            else:
                pairs.remove(']')
        # If the character is an opening bracket
        if char == '[':
            # Set a depth to zero
            depth = 0
            # If the depth is 0 and the current character is ']
            if depth==0:
                # Insert the pair into the set
                pairs.add('[')
            # If the depth is greater than 0, insert into the set
            else:
                pairs.add(']')
        # Increment the depth
        depth += 1
    #If the pairs is empty, the string is valid
    if pairs == set():
        return True
    else:
        return False
