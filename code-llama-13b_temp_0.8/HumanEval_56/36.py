

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

    # Hint: the stack keeps track of the expected next bracket.
    expected = ">"
    for b in brackets:
        if b != expected:
            return False
        else:
            if b == "<":
                expected = ">"
            elif b == ">":
                expected = "<"
    return expected == "<"

