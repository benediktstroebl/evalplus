

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
    counter_opening = 0
    counter_closing = 0

    for bracket in brackets:
        if bracket == '<':
            counter_opening += 1
        elif bracket == '>':
            counter_closing += 1
        else:
            pass

    if counter_opening == counter_closing:
        return True
    else:
        return False

