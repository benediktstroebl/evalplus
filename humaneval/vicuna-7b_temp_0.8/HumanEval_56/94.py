

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
    for opening_brace in brackets:
        if not brackets.count("<", 0, len(opening_brace) + 1):
            return False
        for closing_brace in brackets[brackets.index(opening_brace) + 1:]:
            if not brackets.count(">", 0, len(closing_brace) + 1):
                return False
        if not brackets.count("<", 0, len(opening_brace) + 1) or not brackets.count(">", 0, len(closing_brace) + 1):
            return False
    return True
