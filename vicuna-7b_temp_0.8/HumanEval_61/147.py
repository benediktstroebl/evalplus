

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
    open_brackets = set(brackets)
    for bracket in open_brackets:
        for i in range(1, len(bracket)):
            if bracket[i] != bracket[0]:
                return False
    return True
