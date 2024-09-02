

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
    num_of_open = 0
    num_of_close = 0
    for symbol in brackets:
        if symbol == "(":
            num_of_open += 1
        elif symbol == ")":
            num_of_close += 1
        else:
            continue
    if num_of_open != num_of_close:
        return False
    else:
        return True

