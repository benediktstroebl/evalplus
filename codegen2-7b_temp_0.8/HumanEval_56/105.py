

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
    bracket_list = list(brackets)
    for i in bracket_list:
        if i == "<":
            if bracket_list[bracket_list.index(i)-1]!= ">":
                return False
        elif i == ">":
            if bracket_list[bracket_list.index(i)+1]!= "<":
                return False
    return True
