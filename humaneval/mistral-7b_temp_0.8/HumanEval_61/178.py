

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
    if brackets == "":
        return True
    elif brackets[0] == "(" and correct_bracketing(brackets[1:]) == True:
        return True
    elif brackets[0] == ")" and correct_bracketing(brackets[1:]) == True:
        return True
    elif brackets[0] == ")" and brackets[1:] == "":
        return True
    elif brackets[0] == "(" and brackets[1:] == "":
        return False
    else:
        return False

