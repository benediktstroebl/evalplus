

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
    if len(brackets) == 0:
        return True
    elif brackets[0] == ">" and brackets.count(">") == 1 and brackets.count("<") % 2 == 0:
        return correct_bracketing(brackets[1:])
    elif brackets[0] == "<" and brackets.count("<") == 1 and brackets.count(">") % 2 == 0:
        return correct_bracketing(brackets[1:])
    else:
        return False
