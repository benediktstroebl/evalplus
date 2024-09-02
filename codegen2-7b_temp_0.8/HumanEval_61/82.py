

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
    while brackets:
        if not brackets:
            return False
        closing_bracket = brackets[-1]
        brackets = brackets[:-1]
        if not brackets:
            return True
        if not (closing_bracket == "(" and brackets[0] == ")"):
            return False
        brackets = brackets[1:]
    return
