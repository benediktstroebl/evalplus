

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

    opening_brackets = set()
    closing_brackets = set()
    for bracket in brackets:
        if bracket == ">":
            opening_brackets.add(bracket)
        elif bracket == "<":
            closing_brackets.add(bracket)
    if opening_brackets.difference(closing_brackets):
        return False
    return True

