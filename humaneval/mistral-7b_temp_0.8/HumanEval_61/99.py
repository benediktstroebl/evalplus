

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
    # Recursively run through the string to check each bracket
    brackets = list(brackets)
    if len(brackets) == 0:
        return True
    else:
        if brackets[0] == "(":
            if correct_bracketing(brackets[1:]) == True:
                return True
        elif brackets[0] == ")":
            if correct_bracketing(brackets[1:]) == True:
                return True
        else:
            return False

