

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

    stack = []
    for br in brackets:
        if br == "<":
            stack.append(br)
        else: # br == ">"
            if not stack:
                return False
            else:
                stack.pop()
    return not stack
