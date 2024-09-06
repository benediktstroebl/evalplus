

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
    for b in brackets:
        if b not in (")", "(", "}"):
            return False
        if len(brackets) > 1 and brackets[0] == brackets[-1]:
            return False
    return True
