

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
    for i, x in enumerate(brackets):
        if x == "(":
            brackets[i] = ")"
        elif x == ")":
            if i == 0 or brackets[i - 1]!= "(":
                return False
            brackets.pop()
    return len(brackets) == 0
