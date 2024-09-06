

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
    opened = []

    for bracket in brackets:
        if bracket == "(":
            opened.append(bracket)
        elif bracket == ")":
            if not opened:
                return False
            else:
                opened.pop()
    return not opened
