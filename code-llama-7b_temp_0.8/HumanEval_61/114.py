

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
    for bracket in brackets:
        if bracket == '(':
            level += 1
        elif bracket == ')':
            level -= 1
        if level < 0:
            return False
    return level == 0

