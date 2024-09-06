

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
    # this is not the most efficient way to do this, but it works
    open_brackets = ["<", ">"]
    closing_brackets = open_brackets[::-1]
    for i in range(len(brackets)-1):
        if bracket = bracket