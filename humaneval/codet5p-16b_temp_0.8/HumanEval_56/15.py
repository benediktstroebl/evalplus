

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

    opening_bracketing = 0
    closing_bracketing = 0

    for bracket in brackets:
        if bracket == "<":
            opening_bracketing += 1
        elif bracket == ">":
            closing_bracketing += 1
    
    if opening_bracketing == closing_bracketing:
        return True
    else:
        return False
