

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
    bracket_stack = []
    for bracket in brackets:
        if bracket == "<":
            bracket_stack.append("<")
        else:
            try:
                last_bracket = bracket_stack.pop()
            except IndexError:
                return False
            if bracket != ">":
                return False
    return True

