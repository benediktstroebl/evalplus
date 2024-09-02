

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

    if len(brackets) % 2 == 1:
        return False
    opening_brackets = "<"
    closing_brackets = ">"
    count_opening = 0
    count_closing = 0
    for bracket in brackets:
        if bracket in opening_brackets:
            count_opening += 1
        if bracket in closing_brackets:
            count_closing += 1
    if count_opening == count_closing:
        return True
    else:
        return False
