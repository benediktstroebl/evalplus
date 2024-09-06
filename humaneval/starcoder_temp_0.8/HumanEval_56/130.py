

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

    # # Answer 1
    # return len(brackets) == brackets.count("<") + brackets.count(">")

    # Answer 2
    count = 0
    for br in brackets:
        if br == "<":
            count += 1
        else:
            count -= 1
        if count < 0:
            return False
    return count == 0
