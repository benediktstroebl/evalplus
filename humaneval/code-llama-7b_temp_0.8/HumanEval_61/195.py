

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
    "*** YOUR CODE HERE ***"
    if len(brackets) == 0:
        return True
    elif brackets[0] == "(":
        return correct_bracketing(brackets[1:])
    elif brackets[0] == ")":
        if len(brackets) == 1:
            return False
        elif brackets[1] == "(":
            return correct_bracketing(brackets[2:])
        else:
            return False
    else:
        return False

