

def correct_bracketing(brackets: str):
    """ brackets is a string of "(" and ")".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("(")
    False
    >>> correct_bracketing("()")
    True
    >>> correct_bracketing("(()())")
    True
    >>> correct_bracketing(")(()")
    False
    """

    # Initialize an empty stack
    stack = []

    # Go through each bracket in the string
    for bracket in brackets:
        if bracket == "(":
            # Add opening brackets to the stack
            stack.append("(")
        elif bracket == ")":
            # If the stack is empty, there is no corresponding opening bracket, so return False
            if not stack:
                return False

            # Pop the opening bracket off the stack
            stack.pop()

    # If there are still brackets left in the stack, return False
    return not stack

