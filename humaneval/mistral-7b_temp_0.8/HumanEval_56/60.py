

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

    open_bracket = "<"
    close_bracket = ">"
    stack = []

    for bracket in brackets:
        if bracket == open_bracket:
            stack.append(bracket)
        elif bracket == close_bracket:
            if len(stack) > 0 and stack[-1] == open_bracket:
                stack.pop()
            else:
                return False

    return len(stack) == 0

