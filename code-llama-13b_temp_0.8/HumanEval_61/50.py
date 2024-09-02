

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
    unclosed = 0
    for c in brackets:
        if c == '(':
            unclosed += 1
        if c == ')':
            unclosed -= 1
        if unclosed < 0:
            return False
    return unclosed == 0



