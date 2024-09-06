

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
    for i in brackets:
        if i == "(":
            s.append(i)
        if i == ")":
            if len(s) == 0:
                return False
            else:
                s.pop()
    return len(s) == 0
