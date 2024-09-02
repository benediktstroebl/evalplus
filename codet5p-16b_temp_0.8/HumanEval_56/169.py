

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

    open_brackets = ["<"]
    closed_brackets = [">"]
    for bracket in brackets:
        if bracket in open_brackets:
            open_brackets.remove(bracket)
        elif bracket in closed_brackets:
            closed_brackets.remove(bracket)
        else:
            return False
    if len(open_brackets) == 1:
        return open_brackets[0] == ">"
    else:
        return True



