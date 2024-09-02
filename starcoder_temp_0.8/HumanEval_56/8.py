

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
    # Your code here
    lefts = 0
    rights = 0
    for bracket in brackets:
        if bracket == "<":
            lefts += 1
        else:
            rights += 1
    return lefts == rights
