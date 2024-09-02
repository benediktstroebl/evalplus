

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
    if brackets[0] == "<":
        if len(brackets) == 1:
            return False
        elif len(brackets) == 2:
            if brackets[1] == ">":
                return True
            return False
        elif brackets[1] == ">":
            return correct_bracketing(brackets[2:])
        return False
    elif brackets[0] == ">":
        if len(brackets) == 1:
            return False
        elif len(brackets) == 2:
            if brackets[1] == "<":
                return True
            return False
        elif brackets[1] == "<":
            return correct_bracketing(brackets[2:])
        return False
    return False

