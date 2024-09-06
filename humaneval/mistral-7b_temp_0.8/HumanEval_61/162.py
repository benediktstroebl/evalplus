

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
    opening = []
    closing = []
    for bracket in brackets:
        if bracket == "(":
            opening.append(bracket)
        elif bracket == ")":
            if closing:
                closing.pop()
            else:
                return False
        else:
            return False
    if closing:
        return False
    return True

