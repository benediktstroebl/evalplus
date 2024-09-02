

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
    counter = 0
    for i in brackets:
        if i == ">" and counter < 1:
            return False
        if i == "<":
            counter += 1
        if i == ">":
            counter -= 1
    if counter > 0:
        return False
    if counter == 0:
        return True

