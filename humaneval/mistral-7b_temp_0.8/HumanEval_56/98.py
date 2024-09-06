

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
    opening_brackets = "<>"
    stack = ""
    for bracket in brackets:
        if bracket in opening_brackets:
            stack = stack + bracket
        else:
            if len(stack) == 0:
                return False
            else:
                if stack[-1] == bracket:
                    stack = stack[:-1]
                else:
                    return False
    if len(stack) == 0:
        return True
    return False


