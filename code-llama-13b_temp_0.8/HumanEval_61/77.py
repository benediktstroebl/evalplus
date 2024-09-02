

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

    cnt = 0
    for i in brackets:
        if i == "(":
            cnt += 1
        elif i == ")":
            if cnt == 0:
                return False
            cnt -= 1
    return cnt == 0

