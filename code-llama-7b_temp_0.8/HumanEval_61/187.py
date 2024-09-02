

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
    "*** YOUR CODE HERE ***"

    level = 0
    for c in brackets:
        if c == '(':
            level += 1
        elif c == ')':
            level -= 1
            if level < 0:
                return False
    return level == 0

