

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
    # Hint: Open brackets = 0, Closed brackets = 0 to start with

    # Note: brackets is not a good variable name (too ambiguous)

    # pass
    open_brackets = 0
    closed_brackets = 0
    for b in brackets:
        if b == '(':
            open_brackets += 1
        elif b == ')':
            closed_brackets += 1
    return open_brackets == closed_brackets

