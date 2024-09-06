

def correct_bracketing(brackets: str):
    """ brackets is a string of "<" and ">".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("<")
    False
    >>> correct_bracketing("<>")
    True
    >>> correct_bracketing("<<><>>")
    True
    >>> correct_bracketing("><<>")
    False
    """
    # Create a list of the bracket pairs.
    # Then, create a list of the opening brackets in the string.
    # Create a list of the closing brackets.
    # Add a "0" to the front of each list, so it can be iterated.
    # Iterate through each list and match the pairs.
    # If the lists are of the same length, and every pair is the same,
    # return True, otherwise return False.

    # Use a for loop to iterate through the brackets.
    # Use an if statement to check if the current bracket is an opening bracket.
    # If it is, add it to a list of opening brackets.
    # If it is a closing bracket, add it to a list of closing brackets.
    # If it is neither an opening or closing bracket, return False.
    # If the number of opening brackets is not equal to the number of closing brackets,
    # return False.
    # If the number of opening brackets is equal to the number of closing brackets,
    # return True
