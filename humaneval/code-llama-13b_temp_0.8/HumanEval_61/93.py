

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
    for char in brackets:
        if char == '(':
            open_count += 1
        if char == ')':
            if open_count > 0:
                open_count -= 1
            else:
                return False
    return open_count == 0

