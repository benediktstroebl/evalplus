

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

    l = list(brackets)

    if not l:
        return True

    if l[0] == "<":
        return False

    stack = []
    for b in l:
        if b == "<":
            stack.append(b)
        else:
            if not stack:
                return False
            stack.pop()

    return not stack
