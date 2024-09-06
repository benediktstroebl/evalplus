

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
    brackets = brackets.split("<->")
    if len(brackets) == 1:
        return True
    for i in range(len(brackets) - 1):
        if not brackets[i] == ">" + "<" + ">" or not brackets[i + 1] == "<" + ">":
            return False
    return True
