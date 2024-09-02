

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

    correct_bracketing.i = 0
    correct_bracketing.brackets = brackets
    if correct_bracketing.brackets == "":
        return True
    return correct_bracketing._correct()

