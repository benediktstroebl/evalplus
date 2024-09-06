

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
    if brackets[-1] == "(":
        return correct_bracketing(brackets[:-1])
    elif brackets[-1] == ")":
        return correct_bracketing(brackets[:-1]) and \
               brackets[:-1].count("(") == brackets[:-1].count(")")
    else:
        return False
