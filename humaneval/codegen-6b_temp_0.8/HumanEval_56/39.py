

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
            if index + 1 >= len(brackets):
                return False
            elif brackets[index + 1] == ">":
                index += 1
            else:
                return False
        elif brackets[index] == ">":
            if index - 1 >= 0 and brackets[index - 1] == "<":
                index -= 1
            else:
                return False
        index += 1
    return True
