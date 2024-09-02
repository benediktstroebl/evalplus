

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
    bracketing = {}
    for bracket in brackets:
        if bracket not in bracketing:
            bracketing[bracket] = ""
        bracketing[bracket] += bracket
    for bracket in bracketing:
        if bracketing[bracket]!= bracket:
            return False
    return True
