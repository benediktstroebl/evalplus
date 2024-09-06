

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
    # Hint: Keep track of how many brackets you have seen so far.
    #   When you see a closing bracket and you have not yet seen any opening brackets, then you know that it is not
    #   balanced.
    pass
