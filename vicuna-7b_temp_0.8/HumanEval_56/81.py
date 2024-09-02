

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
    for opening in brackets.strip("<>").split("><"):
        if not brackets.startswith(opening):
            return False
        for closing in brackets.strip("<>").split("><"):
            if closing.startswith(opening):
                if not brackets.endswith(closing):
                    return False
        if not brackets.endswith(opening):
            return False
    return True
