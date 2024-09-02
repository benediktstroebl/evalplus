

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
    s = []
    for b in brackets:
        if b == "(":
            s.append(b)
        elif b == ")":
            if not s:
                return False
            else:
                s.pop()
    return not s
