

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
    if len(brackets) % 2 != 0:
        return False

    left = 0
    for b in brackets:
        if b == '(':
            left += 1
        elif b == ')' and left <= 0:
            return False
        else:
            left -= 1
    return left == 0

