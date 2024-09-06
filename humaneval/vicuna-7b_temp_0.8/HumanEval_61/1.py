

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
    if not brackets:
        return False

    # check if the brackets are closed
    for i, c in enumerate(brackets):
        if c != '(' and c != ')':
            return False

    # check if the brackets are balanced
    if len(brackets) % 2 != 0:
        return False

    return True
