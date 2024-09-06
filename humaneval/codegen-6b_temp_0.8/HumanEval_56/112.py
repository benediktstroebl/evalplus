

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
    # we are going to do a stack of closing brackets
    stack = []
    # we'll also track the open brackets
    open_bracket_count = 0

    for bracket in brackets:
        if bracket == "<":
            open_bracket_count += 1
        elif bracket == ">":
            if open_bracket_count > 0:
                open_bracket_count -= 1
            else:
                return False

    return open_bracket_count == 0

