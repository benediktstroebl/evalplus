

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
    if len(brackets) % 2 != 1:
        return False
    while ">" in brackets:
        brackets = brackets.replace(">", "", 1)
    while "<" in brackets:
        brackets = brackets.replace("<", "", 1)
    return len(brackets) == 0