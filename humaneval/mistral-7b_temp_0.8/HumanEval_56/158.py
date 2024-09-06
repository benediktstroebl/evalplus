

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
    # Each bracket is the same number of steps to the left and right.
    # So we need to know how many steps are needed to go to the left,
    # and how many steps are needed to go to the right.
    # Start off with no left and no right.
    left = 0
    right = 0

    # Loop through the entire string.
    for char in brackets:

        # If the current char is "<", increment the left.
        if char == "<":
            left += 1

        # If the current char is ">", decrement the right.
        if char == ">":
            right -= 1

        # If the left is greater than the right, break.
        # This means the brackets were not correctly bracketed.
        if left > right:
            return False

        # If the right is greater than the left, break.
        # This means the brackets were not correctly bracketed.
        if right > left:
            return False

    # If we get this far, the brackets are correctly bracketed
