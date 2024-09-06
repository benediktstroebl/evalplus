

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
    # return True if every opening bracket has a corresponding closing bracket.
    open_brackets = 0
    close_brackets = 0
    for i in brackets:
        if i == '(':
            open_brackets += 1
        else:
            close_brackets += 1
    return open_brackets == close_brackets

