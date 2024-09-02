

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
    left = 0
    right = 0
    for letter in brackets:
        if letter == "<":
            left += 1
        elif letter == ">":
            right += 1

        if right > left:
            return False

    return left == right

