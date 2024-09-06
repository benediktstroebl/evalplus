

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
    correct = []
    for bracket in brackets:
        if bracket == "(":
            correct.append(")")
        else:
            if len(correct) == 0:
                return False
            else:
                correct.pop()
    if len(correct) == 0:
        return True
    else:
        return False

