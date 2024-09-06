

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
    return all([
        brackets[0] == '(' and brackets[1] == ')',
        brackets[1] == '(' and brackets[2] == ')',
        brackets[2] == '(' and brackets[3] == ')',
        brackets[3] == ')'
    
