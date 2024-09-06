

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
    for i, c in enumerate(brackets):
        if c == "<":
            stack.append(i)
        elif c == ">" and stack:
            stack.pop()
        else:
            return False
    return not stack

