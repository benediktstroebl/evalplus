

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
    # Hint: Keep track of the number of unmatched opening brackets.
    # Hint: Notice that if the number of unmatched open brackets becomes
    #       negative at any point, we know that the bracketing is wrong.
    unmatched = 0
    for b in brackets:
        if b == '(':
            unmatched += 1
        elif b == ')':
            unmatched -= 1
        if unmatched < 0:
            return False
    return unmatched == 0

