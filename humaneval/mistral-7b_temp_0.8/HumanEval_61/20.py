

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
    parenthesis_count = 0
    for char in brackets:
        if char == "(":
            parenthesis_count += 1
        elif char == ")":
            parenthesis_count -= 1
        if parenthesis_count < 0:
            return False
    return parenthesis_count == 0

