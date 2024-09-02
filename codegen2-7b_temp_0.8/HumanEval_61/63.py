

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
    return len(brackets) % 2 == 0 and all(brackets.count(open) == brackets.count(close) for open, close in zip(OPEN_BRACKETS, CLOSE_BRACKETS))
