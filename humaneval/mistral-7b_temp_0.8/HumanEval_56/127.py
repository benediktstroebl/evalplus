

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
    opening_brackets = "<"
    closing_brackets = ">"
    stack = []
    for bracket in brackets:
        if bracket in opening_brackets:
            stack.append(bracket)
        elif bracket in closing_brackets:
            if stack:
                opening_bracket = stack.pop()
            else:
                return False
        else:
            return False

    if not stack:
        return True
    else:
        return False

