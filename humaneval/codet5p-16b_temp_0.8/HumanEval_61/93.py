

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

    bracket_pairs = {}
    for i, bracket in enumerate(brackets):
        if bracket == "(":
            bracket_pairs[i] = bracket
        elif bracket == ")":
            if bracket_pairs.get(i, None)!= "(":
                return False
            del bracket_pairs[i]
    return len(bracket_pairs) == 0
