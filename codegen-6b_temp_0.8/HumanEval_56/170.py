

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
    if not brackets:
        return True

    char, prev = brackets[0], None
    if char == "<" or char == ">":
        return False

    for char in brackets[1:]:
        if char == "<" and prev != ">" or char == ">" and prev != "<":
            return False
        prev = char

    return True

