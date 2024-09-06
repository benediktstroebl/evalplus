

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
    opening = ["<"]
    closing = [">"]
    counter = 0
    for c in brackets:
        if c in opening:
            counter += 1
        elif c in closing:
            counter -= 1
        if counter < 0:
            return False
    return counter == 0

