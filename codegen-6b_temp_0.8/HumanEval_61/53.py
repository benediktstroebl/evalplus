

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
    balanced = None
    start = 0
    while start < len(brackets):
        if not balanced:
            if brackets[start] == "(":
                balanced = "("
            else:
                return False
        else:
            if brackets[start] == ")" and brackets[start + 1] == balanced:
                balanced = None
            else:
                return False
        start += 1

    return True
