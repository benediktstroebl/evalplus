

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
    for open_bracket in brackets:
        for i in range(1, len(open_bracket)):
            if not brackets[i] == open_bracket[0]:
                return False
        if brackets[i] != ")":
            return False
    return True