

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
    no_open, no_close = '', ''
    for b in brackets:
        if b == '(':
            no_open += b
        else:
            no_close += b
    return len(no_open) == len(no_close)

