

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
    open_brackets = set(brackets.split("("))
    close_brackets = set(brackets.split(")")[1:])

    for open_bracket in open_brackets:
        if open_bracket not in close_brackets:
            return False

    return True
