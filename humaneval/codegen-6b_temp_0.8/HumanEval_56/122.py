

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
    i = 0
    while i < len(brackets):
        if brackets[i] == ">" and i + 1 < len(brackets):
            if brackets[i + 1] == "<":
                i += 2
                continue
            else:
                return False
        elif brackets[i] == "<":
            i += 1
            continue
        else:
            return False
    return True
