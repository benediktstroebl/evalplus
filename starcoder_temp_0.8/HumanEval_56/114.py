

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
    s = []
    for c in brackets:
        if c == "<":
            s.append(c)
        elif c == ">":
            if not s:
                return False
            else:
                s.pop()
    return not s
