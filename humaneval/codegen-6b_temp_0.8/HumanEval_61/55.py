

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
    # Count the number of (
    open_bracket = 0
    for character in brackets:
        if character == "(":
            open_bracket += 1
        elif character == ")":
            if open_bracket > 0:
                open_bracket -= 1
            else:
                return False
    if open_bracket > 0:
        return False
    else:
        return True
