

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
    # Can use a stack to keep track of opening brackets.
    # Reset the stack to an empty list at the beginning of each iteration.
    stack = []
    for i, bracket in enumerate(brackets):
        stack.append(bracket)
        if len(stack) > 1:
            # If more than one opening bracket is still
            # present, we haven't found a matching closing bracket.
            return False
        elif i == len(brackets) - 1:
            # If we are at the end of the string, check that
            # the stack is empty.
            if len(stack) == 0:
                return True
