

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

    opens = []
    for bracket in brackets:
        if bracket == "<":
            opens.append(bracket)
        else:
            if len(opens) == 0:
                return False
            else:
                opens.pop()
    if len(opens)!= 0:
        return False
    else:
        return True


