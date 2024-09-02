

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
    for c in brackets:
        if c == "<":
            opens.append(c)
        else:
            if len(opens) == 0:
                return False
            if c!= opens.pop():
                return False
    return len(opens) == 0
