

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
    for ch in brackets:
        if ch == '(':
            s.append('(')
        else:
            if s:
                s.pop()
            else:
                return False
    return not s
