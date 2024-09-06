

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
        if brackets.find("<") > -1:
            if brackets.find(">") == -1:
                return False
            else:
                return correct_bracketing(brackets[brackets.find(">") + 1:])
        elif brackets.find(">") > -1:
            return False
        else:
            return True

