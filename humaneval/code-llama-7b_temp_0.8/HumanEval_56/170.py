

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
    depth = 0
    for c in brackets:
        if c == '<':
            depth += 1
        elif c == '>' and depth > 0:
            depth -= 1
        else:
            return False
    return depth == 0

