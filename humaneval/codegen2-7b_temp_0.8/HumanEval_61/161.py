

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
    if not brackets or brackets[0]!= "(" or brackets[-1]!= ")":
        return False
    brackets = brackets[1:-1]
    for b in brackets:
        if b not in "()":
            return False
    return True
