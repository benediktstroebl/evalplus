

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
    for i, b in enumerate(brackets):
        if b == ">" and not stack:
            return False
        elif b == "<" and stack:
            stack.pop()
        else:
            stack.append(i)
    return not stack

