

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
    left = 0
    for c in brackets:
        if c == '(':
            left += 1
        elif c == ')':
            if left == 0:
                return False
            left -= 1
    return left == 0

