

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
    num_brackets = 0

    for char in brackets:
        if char == "<":
            num_brackets += 1
        if char == ">":
            num_brackets -= 1

    if num_brackets == 0:
        return True
    else:
        return False

