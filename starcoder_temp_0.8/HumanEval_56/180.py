

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

    opening_brackets = [i for i in range(len(brackets)) if brackets[i] == "<"]
    closing_brackets = [i for i in range(len(brackets)) if brackets[i] == ">"]

    for o in opening_brackets:
        if not (o + 1 in closing_brackets):
            return False
    return True
