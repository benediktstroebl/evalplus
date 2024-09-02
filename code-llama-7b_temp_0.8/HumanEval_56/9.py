

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
    num_opening = 0
    for char in brackets:
        if char == '<':
            num_opening += 1
        elif char == '>' and num_opening > 0:
            num_opening -= 1
        else:
            return False
    return num_opening == 0
