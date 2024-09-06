

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
    if len(brackets) % 2 == 1:
        return False
    index = 0
    while index < len(brackets):
        if brackets[index] == "<":
            if index + 1 >= len(brackets):
                return False
            if brackets[index + 1] == ">":
                index += 2
            else:
                return False
        else:
            index += 1
    return True
