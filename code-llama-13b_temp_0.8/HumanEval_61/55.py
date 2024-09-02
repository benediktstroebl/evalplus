

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
    num_open = 0
    for c in brackets:
        if c == '(':
            num_open += 1
        elif c == ')':
            num_open -= 1
        if num_open < 0:
            return False
    return num_open == 0

