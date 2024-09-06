

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
    # an empty string is correct
    if len(brackets) == 0:
        return True

    # keep track of the current number of opening brackets
    num_opening = 0

    # a loop that counts up as it finds opening brackets, and counts down as it finds closing brackets
    for char in brackets:
        if char == "<":
            num_opening += 1
        elif char == ">":
            num_opening -= 1
            if num_opening < 0:
                return False
    return num_opening == 0
