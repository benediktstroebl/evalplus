

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
    if len(brackets) % 2 == 1:
        return False

    stack = []
    for bracket in brackets:
        if bracket == "(":
            stack.append(0)
        elif bracket == ")":
            if len(stack) == 0:
                return False
            stack.pop()
    if len(stack) != 0:
        return False
    return True
