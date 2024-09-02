

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

    bracketing = []
    for i in brackets:
        if i == "(":
            bracketing.append(i)
        elif i == ")":
            if len(bracketing) == 0 or bracketing.pop()!= "(":
                return False
    if len(bracketing) == 0:
        return True
    else:
        return False

