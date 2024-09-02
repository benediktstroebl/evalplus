

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
    assert isinstance(brackets, str) and set(brackets) == set("<>")
    opening_brackets = [b for b in brackets if b == "<"]
    closing_brackets = [b for b in brackets if b == ">"]

    if len(opening_brackets) > len(closing_brackets):
        return False

    for b in opening_brackets:
        if closing_brackets.pop(0)!= b:
            return False

    return True
