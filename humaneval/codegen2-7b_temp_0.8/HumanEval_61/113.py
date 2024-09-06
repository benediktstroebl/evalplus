

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
    match_stack = []
    for bracket in brackets:
        if bracket == "(":
            match_stack.append(bracket)
        else:
            if len(match_stack) == 0:
                return False
            match_stack.pop()

    if len(match_stack) == 0:
        return True
    else:
        return False
