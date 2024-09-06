

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

    open_stack = []
    for bracket in brackets:
        if bracket == "<":
            open_stack.append(bracket)
        elif bracket == ">":
            if not open_stack:
                return False
            else:
                open_stack.pop()
    return not open_stack
