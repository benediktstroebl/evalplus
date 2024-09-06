

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
    brackets_list = list(brackets)
    opened_brackets = []
    closed_brackets = []

    for bracket in brackets_list:
        if bracket == "<":
            opened_brackets.append(bracket)
        else:
            closed_brackets.append(bracket)

    for opened in opened_brackets:
        if opened not in closed_brackets:
            return False

    return True

