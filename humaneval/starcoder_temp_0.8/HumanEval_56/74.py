

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
    
    # use a stack to save opening brackets
    s = []

    for b in brackets:
        if b == "<":
            s.append(b)
        else:
            if len(s) == 0:
                return False
            s.pop()
    
    return len(s) == 0

