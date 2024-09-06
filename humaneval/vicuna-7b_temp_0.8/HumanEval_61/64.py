

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
    for open_brace in brackets:
        if not brackets.count(")"):
            return False
        elif not brackets.count(open_brace):
            return False
        elif open_brace == ")":
            if not brackets.count("("):
                return False
        else:
            if not brackets.count("{"):
                return False
            if not brackets.count("}"):
                return False
    return True
