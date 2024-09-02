

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

    # This is a hint for where to get started.
    # The first thing we need to know is how many brackets are open
    # to start, and we start by assuming there aren't any.
    num_open = 0

    # Now we walk through each character in the string.
    # If we see "<", we add one to the `num_open` counter.
    # If we see ">", we subtract one.
    for c in brackets:
        if c == "<":
            num_open += 1
        if c == ">":
            num_open -= 1

    # If we get to the end and there are still brackets open,
    # we know that the brackets are not balanced.
    if num_open > 0:
        return False
    else:
        return True

