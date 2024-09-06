

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

    open_brackets = []
    for i, bracket in enumerate(brackets):
        if bracket == ">":
            open_brackets.append(i)
        elif bracket == "<":
            if len(open_brackets) > 0:
                open_brackets.pop()
            else:
                return False
    return len(open_brackets) == 0
