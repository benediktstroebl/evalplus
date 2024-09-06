

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
    open = 0
    for char in brackets:
        if char == "(":
            open += 1
        elif char == ")":
            open -= 1
        if open < 0:
            return False
    return open == 0
