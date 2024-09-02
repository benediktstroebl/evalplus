

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
    for i, b in enumerate(brackets):
        if b == "(":
            stack.append(i)
        elif b == ")":
            if not stack:
                return False
            stack.pop()
    return True if not stack else False

