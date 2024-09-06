

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
    if len(brackets) < 2:
        return False
    return all(brackets[i] == ">" for i in range(len(brackets) - 1) if brackets[i] == "<") and brackets[0] == "<" and brackets[-1] == ">"
