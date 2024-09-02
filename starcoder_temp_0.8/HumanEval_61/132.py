

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
        brackets[i] == ")" and brackets[i - 1] == "("
        for i in range(1, len(brackets))
        if brackets[i] == ")"
    ])
