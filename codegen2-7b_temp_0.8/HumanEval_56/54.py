

def correct_bracketing(brackets: str):
    """ brackets is a string of "<" and ">".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("<")
    False
    >>> correct_bracketing("<>")
    True
    >>> correct_bracketing("<<><>>")
    True
    >>> correct_bracketing("><<>")
    False
    """
    assert brackets[0] == '<', "There must be at least 1 opening bracket."
    assert brackets[-1] == '>', "There must be at least 1 closing bracket."
    for s in brackets:
        assert s in "<>", "There is no closing bracket for the opening one."
    return all(chr(ord(s) - 1) == chr(ord(s) + 1) for s in brackets)
