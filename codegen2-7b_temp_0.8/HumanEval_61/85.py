

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
    opening = set("({[")
    closing = set(")]}")
    correct = opening.issubset(closing)
    for bracket in brackets:
        correct = correct and opening.issubset({bracket})
    return
