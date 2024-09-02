

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
    if len(brackets) == 0:
        return True
    elif len(brackets) % 2 != 0:
        return False
    else:
        opening = []
        closing = []
        for bracket in brackets:
            if bracket == "(":
                opening.append(bracket)
            elif bracket == ")":
                closing.append(bracket)
        for bracket in opening:
            if bracket not in closing:
                return False
        for bracket in closing:
            if bracket not in opening:
                return False
        return True

