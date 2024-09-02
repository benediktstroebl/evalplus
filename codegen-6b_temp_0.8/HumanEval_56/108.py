

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
    r = {"<": ">", ">": "<"}
    if brackets == "":
        return True
    elif len(brackets) % 2 != 0:
        return False
    elif brackets[0] in r:
        return correct_bracketing(brackets[1:])
    return False
