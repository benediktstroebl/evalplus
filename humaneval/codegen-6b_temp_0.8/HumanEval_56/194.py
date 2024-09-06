

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
    "*** YOUR CODE HERE ***"
    star_left  = 0
    star_right = 0

    for i in brackets:
        if i == "<":
            star_left += 1
        elif i == ">":
            star_right += 1

    if star_left != star_right:
        return False
    return True
