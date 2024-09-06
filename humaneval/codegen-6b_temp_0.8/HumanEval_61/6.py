

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
    num_open_bracket = 0
    for bracket in brackets:
        if bracket == '(':
            num_open_bracket += 1
        if bracket == ')':
            if num_open_bracket == 0:
                return False
            num_open_bracket -= 1
    return num_open_bracket == 0
