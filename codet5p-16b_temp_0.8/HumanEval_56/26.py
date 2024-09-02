

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

    while "<<" in brackets or ">>" in brackets:
        brackets = brackets.replace("<<", "")
        brackets = brackets.replace(">>", "")
    return len(brackets) == 0
