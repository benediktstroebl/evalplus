

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
    opens = []
    for b in brackets:
        if b == "<":
            opens.append(b)
        elif b == ">":
            if len(opens) == 0:
                return False
            else:
                opens.pop()
    return len(opens) == 0
