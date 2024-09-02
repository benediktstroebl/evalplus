

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
    for char in brackets:
        if not char in '()':
            return False
    if brackets == "":
        return True
    return correct_bracketing(brackets[1:]) and correct_bracketing(brackets[:-1
