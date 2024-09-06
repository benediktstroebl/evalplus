

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
    # state = 0 -> "no opening bracket encountered yet"
    # state = 1 -> "opening bracket encountered"
    # state = 2 -> "closing bracket encountered"

    state = 0
    for c in brackets:
        if c == '<':
            if state == 2:
                return False
            state = 1
        elif c == '>':
            if state == 1:
                state = 0
            else:
                return False
        else:
            assert False
    return state == 0

