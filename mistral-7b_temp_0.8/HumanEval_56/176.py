

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
    for bracket in brackets:
        if bracket == "<":
            open_brackets.append(bracket)
        elif bracket == ">":
            if open_brackets:
                open_brackets.pop()
            else:
                return False
    return not open_brackets

