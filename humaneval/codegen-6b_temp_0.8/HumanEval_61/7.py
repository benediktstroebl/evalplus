

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
    current_count = 0
    for char in brackets:
        if char == "(":
            current_count += 1
        if char == ")":
            current_count -= 1
        if current_count < 0:
            return False
    return current_count == 0

