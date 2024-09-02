

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

    brackets = list(brackets)
    n = 0
    while n < len(brackets):
        if brackets[n] == "(":
            brackets[n] = ")"
        n += 1
    n = 0
    while n < len(brackets):
        if brackets[n] == ")":
            brackets[n] = "("
        n += 1
    return brackets == ["("]
