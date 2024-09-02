

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
    if len(brackets) == 0 or len(brackets) % 2 != 0:
        return False

    counter = 0
    for b in brackets:
        if b == '(':
            counter += 1
        else:
            if counter == 0:
                return False
            counter -= 1
    return True
