

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
    # for char in brackets:
    #     if not char in "<>":
    #         return False
    # return True
    bracket_list = list(brackets)
    for bracket in bracket_list:
        if not bracket in "<>":
            return False
    return True

