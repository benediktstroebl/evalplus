

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

    assert len(brackets) == 2
    correct = True
    count = 0
    for bracket in brackets:
        if bracket == ">" and count == 0:
            correct = False
        elif bracket == "<" and count > 0:
            correct = False
        elif bracket == "<" and count == 0:
            count += 1
        else:
            count -= 1

    return correct
