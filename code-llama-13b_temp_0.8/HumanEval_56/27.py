

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
    num_opened = 0
    for char in brackets:
        if char == "<":
            num_opened += 1
        else:
            num_opened -= 1
            if num_opened < 0:
                return False
    if num_opened != 0:
        return False
    return True
