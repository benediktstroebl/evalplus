

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
    new_brackets = ""
    for bracket in brackets:
        if bracket in "<>":
            new_brackets += ">"
        new_brackets += bracket

    return new_brackets[::2] == new_brackets[1::2]
