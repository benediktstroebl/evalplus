

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
    if len(brackets) % 2 != 0:
        return False

    opening = "{}<>"
    closing = "{}>"

    # opening = "".join(brackets)
    # closing = "".join(brackets[::-1])

    if brackets == opening:
        return False
    if brackets == closing:
        return False
    if brackets[0] == ">" or brackets[-1] == "<":
        return False

    return brackets == opening + closing

