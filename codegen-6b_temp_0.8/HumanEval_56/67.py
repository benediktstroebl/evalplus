

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
    contains_sensible = True
    for idx, character in enumerate(brackets):
        if character == "<":
            if not (idx < len(brackets) - 1 and brackets[idx + 1] == ">"):
                contains_sensible = False
                break
    return contains_sensible

