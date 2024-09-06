

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
    open_brackets = set("<[{(")
    close_brackets = set("}])>")

    s = ""
    for b in brackets:
        if b in open_brackets:
            s += b
        elif b in close_brackets:
            if not s:
                return False
            else:
                s = s[:-1]
        else:
            return False
    return not s
