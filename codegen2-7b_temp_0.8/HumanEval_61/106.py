

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
    open_brackets = ''.join(['(', ')'])
    if len(brackets) % 2 == 1:
        return False
    for bracket in brackets:
        if bracket not in open_brackets:
            return False
    return True

