

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
    while brackets:
        if brackets[0] == ")" and not brackets[1] == ")":
            return False
        if brackets[-1] == "(":
            return False
        brackets = brackets[1:-1]
    return True
