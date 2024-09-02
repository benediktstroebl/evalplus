

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
    output = []
    for c in brackets:
        if c == ">":
            output.append(c)
        elif c == "<":
            if len(output) == 0:
                return False
            else:
                output.pop()
    if len(output) == 0:
        return True
    return False
