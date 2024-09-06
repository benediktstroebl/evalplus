

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
    elif brackets[0] == "<" and brackets[len(brackets) - 1] == ">":
        brackets = brackets[1:-1]
        return correct_bracketing(brackets)
    elif brackets[0] == "<" and brackets[len(brackets) - 1] != ">":
        return False
    elif brackets[0] != "<" and brackets[len(brackets) - 1] == ">":
        return False
    else:
        return correct_bracketing(brackets[1:len(brackets) - 1])

