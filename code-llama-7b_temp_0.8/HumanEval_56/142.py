

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

    # the idea is to count the number of "<"s and ">"s, and compare them.

    num_left_brackets = 0
    num_right_brackets = 0

    for c in brackets:
        if c == "<":
            num_left_brackets += 1
        elif c == ">":
            num_right_brackets += 1
        else:
            return False

    return num_left_brackets == num_right_brackets

