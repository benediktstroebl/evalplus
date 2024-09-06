

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
    for opening in brackets:
        if not brackets:
            return False
        for closing in brackets[1:]:
            if bracket_match(opening, closing):
                if not bracket_match(opening[1:], closing[1:]):
                    return False
            else:
                return False
    return True
