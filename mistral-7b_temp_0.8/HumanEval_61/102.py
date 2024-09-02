

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
    left_count = 0
    for ch in brackets:
        if ch == '(':
            left_count += 1
        elif ch == ')':
            left_count -= 1
            if left_count < 0:
                return False
    return left_count == 0

