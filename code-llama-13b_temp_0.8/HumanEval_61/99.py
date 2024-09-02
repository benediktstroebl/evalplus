

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
    # start each bracket with a count of zero
    # start with an empty list to store all counts for each bracket
    counts = [0, 0]
    for bracket in brackets:
        # for each bracket, increment the appropriate count
        if bracket == "(":
            counts[0] += 1
        else:
            counts[1] += 1

    return counts[0] == counts[1]
