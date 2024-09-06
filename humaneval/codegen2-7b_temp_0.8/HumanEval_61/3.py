

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
    correct = True
    for i in range(len(brackets)-1):
        if brackets[i]!= ')' or brackets[i+1]!= '(':
            correct = False
            break
    return correct
