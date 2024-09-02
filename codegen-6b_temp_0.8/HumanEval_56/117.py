

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
    brackets = brackets.strip()
    outside_chars = [">","<"]
    if len(brackets) == 0:
        return True
    if brackets[0] in outside_chars:
        return False
    else:
        char = brackets[0]
        if brackets.count(char) == 1:
            return True
        else:
            return False
