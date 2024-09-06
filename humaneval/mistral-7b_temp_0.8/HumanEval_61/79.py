

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
    if len(brackets) % 2 != 0:
        return False
    s = []
    for bracket in brackets:
        if bracket == "(":
            s.append("(")
        elif bracket == ")":
            if len(s) > 0 and s[-1] == "(":
                s.pop()
            else:
                return False
    return len(s) == 0

