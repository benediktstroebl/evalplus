

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
    # check for a single opening bracket
    if len(brackets) == 1:
        return brackets[0] == "("
    
    # check for all pairs of opening and closing brackets
    for i in range(1, len(brackets)):
        # check for the current opening bracket
        if brackets[i-1] != "(":
            return False
        # check for the corresponding closing bracket
        if i == len(brackets)-1:
            return False
        # check for the next opening bracket
        if brackets[i+1] != ")":
            return False
        # check for the corresponding closing bracket
        if i == 0:
            return False
    # all opening and closing brackets are paired, so return True
    return True
