

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
    # for each opening bracket, we need to find a corresponding closing bracket.
    # for each opening bracket, we can look at the following characters until we find a corresponding closing bracket.
    # We can't look at any character before the current opening bracket.
    # This is a "greedy" algorithm.
    # Can we think of a way to do this in linear time?
    # Hint: consider what would happen if the string were split into pairs of opening and closing brackets.
    #       does that help?
    return correct_bracketing_helper(brackets, 0)

