

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

    n_open = 0
    for c in brackets:
        if c == '(':
            n_open += 1
        elif c == ')':
            n_open -= 1
        if n_open < 0:
            return False
    return n_open == 0

