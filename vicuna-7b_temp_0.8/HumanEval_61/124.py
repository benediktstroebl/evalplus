

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
    for b in brackets:
        if b == "(":
            stack.append(0)
        elif b == ")":
            if not stack:
                return False
            top = stack.pop()
            if top != 0:
                return False
        else:
            stack.append(b)
    return not stack, stack
