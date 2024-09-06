

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
    bracket_counter = 0
    for b in brackets:
        if b == "(":
            bracket_counter += 1
        else:
            bracket_counter -= 1
        if bracket_counter < 0:
            return False
    return bracket_counter == 0

