

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
    no_of_brackets = 0
    for bracket in brackets:
        if bracket == "<":
            no_of_brackets += 1
        elif bracket == ">":
            no_of_brackets -= 1
    return no_of_brackets == 0
