

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
    level = 0
    for b in brackets:
        if b == '(':
            level += 1
        elif b == ')':
            if level == 0:
                return False
            level -= 1
    return level == 0

