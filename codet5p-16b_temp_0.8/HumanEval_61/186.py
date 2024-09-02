

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

    bracket_dict = {}
    for bracket in brackets:
        if bracket in bracket_dict:
            bracket_dict[bracket] += 1
        else:
            bracket_dict[bracket] = 1
    
    for bracket in bracket_dict:
        if bracket_dict[bracket]!= 1:
            return False
    return True

