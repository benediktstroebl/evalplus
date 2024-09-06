

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
    start = 0
    end = len(brackets)
    while start < end:
        if brackets[start] == ">" and start + 1 < end and brackets[start+1] == "<":
            start += 2
        else:
            return False
    return True