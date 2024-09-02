

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
    left = 0
    right = 0

    for b in brackets:
        if b == "<":
            left += 1
        elif b == ">":
            right += 1
        if left == right:
            continue
        elif left > right:
            return False
    return True
