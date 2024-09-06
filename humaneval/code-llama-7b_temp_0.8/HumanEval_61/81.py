

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
    counter = 0
    for s in brackets:
        if s == "(":
            counter += 1
        if s == ")":
            counter -= 1
            if counter < 0:
                return False
    return counter == 0

