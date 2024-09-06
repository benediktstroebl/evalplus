

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
    for char in brackets:
        if char == "<":
            if not stack:
                return False
            stack.pop()
        elif char == ">":
            stack.append(char)
    if not stack:
        return True
    else:
        return False
