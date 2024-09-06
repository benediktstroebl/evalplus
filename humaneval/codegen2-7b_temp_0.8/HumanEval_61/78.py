

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
    if len(brackets) % 2 == 1:
        return False
    pair = 0
    for c in brackets:
        if c == "(":
            pair += 1
        elif c == ")":
            pair -= 1
            if pair < 0:
                return False
    return pair == 0
