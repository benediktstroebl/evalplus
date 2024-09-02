

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
    # Set of open brackets
    bracket_stack = []
    for b in brackets:
        if b == "<":
            bracket_stack.append(b)
        else:
            if len(bracket_stack) == 0:
                return False
            top = bracket_stack.pop()
            if top != "<":
                return False
    return len(bracket_stack) == 0
