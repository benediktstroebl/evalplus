

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
    count = 0

    for x in brackets:
        if x == "(":
            count += 1
        elif x == ")":
            count -= 1

        if count < 0:
            return False

    return count == 0

