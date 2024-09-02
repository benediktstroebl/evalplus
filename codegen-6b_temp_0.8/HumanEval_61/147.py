

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
    stack = []
    for bracket in brackets:
        if bracket == ")":
            if len(stack) == 0:
                return False
            else:
                top = stack.pop()
                if (top != "("):
                    return False
        else:
            stack.append(bracket)
    if len(stack) > 0:
        return False
    else:
        return True
