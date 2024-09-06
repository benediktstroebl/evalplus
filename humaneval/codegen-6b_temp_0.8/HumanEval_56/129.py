

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
    while brackets:
        if "<" not in brackets:
            return False
        elif "[" in brackets:
            brackets = brackets.replace("<", "]", 1)
        elif "{" in brackets:
            brackets = brackets.replace("{", "}", 1)
        elif "(" in brackets:
            brackets = brackets.replace("(", ")", 1)
    return False
