

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
    if not brackets:
        return False

    for opening in brackets:
        for closing in brackets:
            if opening != closing:
                return False

        if brackets.index(opening) == len(brackets) - 1:
            return False

        if not bracket_matches_opening(brackets, opening):
            return False

    return True