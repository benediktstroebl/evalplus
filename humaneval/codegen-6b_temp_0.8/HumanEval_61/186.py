

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
    for e in brackets:
        if e == "(":
            counts[e] = 1
        elif e == ")":
            if counts.get(e) == 1:
                del counts[e]
            else:
                counts[e] = 1
    return len(counts) == 0