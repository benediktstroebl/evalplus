

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
    index = 0
    while index < len(brackets):
        if brackets[index] == "<":
            index2 = brackets.find(">", index)
            if index2 == -1:
                return False
        index += 1
    return True

