

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

    bracket_stack: list = []

    for bracket in brackets:
        if bracket == "<":
            bracket_stack.append(bracket)
        else:
            if not bracket_stack:
                return False
            bracket_stack.pop()

    return len(bracket_stack) == 0
