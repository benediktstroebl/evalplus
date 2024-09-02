

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
    i = 0
    while i < len(brackets) and brackets[i] == "(":
        i += 1
    j = 0
    while j < len(brackets) and brackets[j] == ")":
        j += 1
    if i == len(brackets) and j == len(brackets):
        return True
    return False
