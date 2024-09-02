

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
    assert all(b in "<>" for b in brackets)
    num_opened = 0
    for b in brackets:
        if b == "<":
            num_opened += 1
        else:
            num_opened -= 1
        if num_opened < 0:
            return False
    return num_opened == 0

