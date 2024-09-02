

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
    for i, ch in enumerate(brackets):
        if ch == '(':
            if i == len(brackets) - 1:
                return True
            if not brackets[i+1] == ')':
                return False
        if ch == ')':
            if not brackets[i-1] == '(':
                return False
    return True

