

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

    bracket_count = 0
    open_bracket_count = 0
    for char in brackets:
        if char == "(":
            open_bracket_count += 1
        elif char == ")":
            bracket_count += 1

    if bracket_count!= open_bracket_count:
        return False
    else:
        return True

