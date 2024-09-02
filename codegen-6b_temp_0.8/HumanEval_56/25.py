

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
    if brackets == "":
        return True
    else:
        count = 0
        for bracket in brackets:
            if bracket == "<":
                count += 1
            elif bracket == ">":
                count -= 1
            else:
                return False
        return count == 0

