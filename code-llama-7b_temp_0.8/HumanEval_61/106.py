

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
    open_count = 0
    for ch in brackets:
        if ch == '(':
            open_count += 1
        elif ch == ')':
            if open_count == 0:
                return False
            open_count -= 1
    return open_count == 0

