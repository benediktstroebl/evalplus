

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
    if not brackets:
        return True

    open_count = 0

    for char in brackets:
        if char == "(":
            open_count += 1
        elif char == ")":
            if open_count == 0:
                return False
            open_count -= 1

    return open_count == 0

