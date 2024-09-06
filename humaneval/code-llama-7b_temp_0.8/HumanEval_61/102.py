

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
    pairs = 0
    for c in brackets:
        if c == '(':
            pairs += 1
        else:
            pairs -= 1
        if pairs < 0:
            return False
    return pairs == 0

