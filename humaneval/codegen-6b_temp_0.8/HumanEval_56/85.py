

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
    start = 0
    matching_pairs = {}
    for i, e in enumerate(brackets):
        if e == ">" and start == 0:
            start = i
        elif e == "<":
            if start in matching_pairs:
                del matching_pairs[start]
            start = 0
    return len(matching_pairs) == 0
