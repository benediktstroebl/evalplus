

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
    # Hint: Keep track of a counter `open` that is incremented by
    #   every opening bracket and decremented by every closing bracket.
    # Hint: If at the end of the string `open` is 0,
    #   then every opening bracket has a corresponding closing bracket.
    open = 0
    for b in brackets:
        if b == '(':
            open += 1
        elif b == ')':
            if open == 0:
                return False
            open -= 1
    if open == 0:
        return True
    return False

