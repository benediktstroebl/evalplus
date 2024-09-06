

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
    stack = 0
    for ch in brackets:
        if ch == "(":
            stack += 1
        elif ch == ")":
            if stack == 0:
                return False
            stack -= 1
    return stack == 0


