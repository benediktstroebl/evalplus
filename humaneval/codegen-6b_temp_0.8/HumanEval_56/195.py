

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
    indices = [i for i, c in enumerate(brackets) if c == ">"]
    if indices:
        if indices[-1] == len(brackets) - 1:
            return True
        if indices[-1] != len(brackets) - 2:
            return False

        if brackets[indices[-1] + 1] == ">":
            return True
        else:
            return False
    else:
        return True

