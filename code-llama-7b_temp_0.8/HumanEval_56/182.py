

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
    # count the "<"s and ">"s and make sure that they're equal
    num_opening, num_closing = 0, 0
    for bracket in brackets:
        if bracket == "<":
            num_opening += 1
        else:
            num_closing += 1

    return num_opening == num_closing
