

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
    flag = True
    if brackets == "":
        flag = False
    elif len(brackets)%2 != 0:
        flag = False
    else:
        openings = 0
        closings = 0
        for b in brackets:
            if b == "<":
                openings += 1
            elif b == ">":
                closings += 1
            if closings > openings:
                flag = False
        if openings > closings:
            flag = False

    return flag




