

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

    for bracket in brackets:
        if bracket == ")" and not brackets.count("("):
            return False
        if bracket == "(" and not brackets.count(")"):
            return False
    return True

