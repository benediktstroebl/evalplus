

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
    if (
        len(brackets) % 2 != 0
    ):  # odd number of characters means there is a mismatch in opening/closing
        return False
    else:
        index = 0
        while index < len(brackets) - 1:
            if brackets[index] == ">" and brackets[index + 1] != "<":
                return False
            index += 1
        return True

