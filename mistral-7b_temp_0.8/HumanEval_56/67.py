

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
    current_level = 0
    for b in brackets:
        if b == "<":
            current_level += 1
        else:
            if current_level == 0:
                return False
            current_level -= 1
    return current_level == 0

