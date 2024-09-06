

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

    # Accumulate the number of open brackes as we progress
    # through the string.
    num_open = 0
    for ch in brackets:
        if ch == '(':
            num_open += 1
        elif ch == ')':
            num_open -= 1
        if num_open < 0:
            return False
    return num_open == 0

