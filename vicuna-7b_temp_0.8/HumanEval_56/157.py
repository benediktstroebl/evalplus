

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
    open_brackets = set(brackets.split(" "))
    for i, bracket in enumerate(open_brackets):
        if bracket == ">":
            if i == len(open_brackets) - 1:
                return False
        elif bracket == "<":
            if i == 0:
                return False
    return True
