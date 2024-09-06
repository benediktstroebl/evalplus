

def correct_bracketing(brackets: str):
    """ brackets is a string of "(" and ")".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("(")
    False
    >>> correct_bracketing("()")
    True
    >>> correct_bracketing("(()())")
    True
    >>> correct_bracketing(")(()")
    False
    """

    open_bracket_list = []
    for bracket in brackets:
        if bracket == "(":
            open_bracket_list.append(bracket)
        elif bracket == ")":
            if len(open_bracket_list) > 0:
                open_bracket_list.pop()
            else:
                return False
    if len(open_bracket_list) == 0:
        return True
    else:
        return False

