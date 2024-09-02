

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
    counts = {}
    for bracket in brackets:
        counts[bracket] = counts.get(bracket, 0) + 1
    return all(count == 0 for count in counts.values())

