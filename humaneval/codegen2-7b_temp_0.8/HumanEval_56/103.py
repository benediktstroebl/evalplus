

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
    if len(brackets) % 2!= 0:
        return False
    left = right = 0
    for c in brackets:
        if c == '<':
            if right > 0:
                return False
            right += 1
        elif c == '>':
            left += 1
            if left > right:
                return False
    return left == right
