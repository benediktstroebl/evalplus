

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
    assert isinstance(brackets, str)
    if len(brackets) == 0: return True
    return (brackets[-1] == ">" and "<" in brackets) and correct_bracketing(brackets[:-1])

