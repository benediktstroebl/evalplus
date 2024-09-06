

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
    matching = []
    for char in brackets:
        if char == "(":
            matching.append(")")
        else:
            if not matching:
                return False
            else:
                matching.pop()
    return not matching

