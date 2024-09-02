

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
    count_l, count_r = 0, 0
    for b in brackets:
        if b == "(":
            count_l += 1
        elif b == ")":
            count_r += 1
        if count_l!= count_r:
            return False
    return count_r == count_l
