

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
    opening_brackets = list(brackets)
    for char in opening_brackets:
        if char!= ')':
            opening_brackets.remove(char)
    if opening_brackets:
        return False
    else:
        return True
