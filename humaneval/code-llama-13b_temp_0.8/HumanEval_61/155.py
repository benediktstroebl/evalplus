

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
    # Make sure all brackets are valid, and then check for an even number
    bracket_stack = []
    for bracket in brackets:
        if bracket == "(":
            bracket_stack.append(bracket)
        elif bracket == ")":
            if len(bracket_stack) > 0:
                bracket_stack.pop()
            else:
                return False
    if len(bracket_stack) % 2 != 0:
        return False
    return True

