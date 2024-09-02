

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
    opening = "><"
    closing = "<>"
    brackets = brackets.strip()
    if len(brackets) % 2 != 0:
        return False
    for i in range(0, len(brackets), 2):
        if brackets[i:i + 2] not in opening + closing:
            return False
        if brackets[i] not in brackets[i + 1]:
            return False
    return True

