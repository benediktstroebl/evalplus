

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
    # Your code here
    if len(brackets) == 0:
        return True
    elif len(brackets) == 1:
        if brackets[0] == "(":
            return False
        else:
            return True
    else:
        if brackets[0] == "(":
            return correct_bracketing(brackets[1:])
        else:
            return False

