

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
    opening_brackets = 0
    for c in brackets:
        if c == "<":
            opening_brackets += 1
        elif c == ">" and opening_brackets > 0:
            opening_brackets -= 1
        elif c == ">" and opening_brackets == 0:
            return False
    return opening_brackets == 0

