

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
    opening_brackets = set(brackets.split("("))
    closing_brackets = set(brackets.split(")")[::-1])
    if opening_brackets == closing_brackets:
        return True
    else:
        return False
