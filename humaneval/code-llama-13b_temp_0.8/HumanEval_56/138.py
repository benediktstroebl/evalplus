

def correct_bracketing(brackets: str):
    """ brackets is a string of "<" and ">".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("<")
    False
    >>> correct_bracketing("<>")
    True
    >>> correct_bracketing("<<><>>")
    True
    >>> correct_bracketing("><<>")
    False
    """

    # Invariants:
    # - so_far has some number of "<" and ">"
    # - every "<" in so_far has a matching ">"
    # - so_far is a string of "<" and ">"
    # - for all i in range(len(so_far)), so_far[:i] has the same properties.

    so_far = ""

    for b in brackets:
        if b == "<":
            so_far += b
        elif b == ">":
            if len(so_far) == 0:
                return False
            if so_far[-1] == "<":
                so_far = so_far[:-1]
            else:
                return False
        else:
            return False

    return len(so_far) == 0

