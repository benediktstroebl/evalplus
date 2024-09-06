

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
    left = []
    right = []
    for bracket in brackets:
        if bracket == "<":
            left.append(bracket)
        elif bracket == ">":
            right.append(bracket)
    if len(left) != len(right):
        return False
    for i, (left_bracket, right_bracket) in enumerate(zip(left, right)):
        if left_bracket != right_bracket:
            return False
    return True

