

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
    if len(brackets) < 2:
        return False
    if len(brackets) % 2 != 0:
        return False

    count = 0
    for char in brackets:
        if char == "(":
            count += 1
        elif char == ")":
            count -= 1
        else:
            return False
        if count < 0:
            return False
    return count == 0