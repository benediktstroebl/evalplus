

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

    opening_brackets = brackets.count('<')

    if opening_brackets == 0:
        return True

    # If there's an odd number of opening brackets, it can't be valid.
    if opening_brackets % 2!= 0:
        return False

    count = 0
    for bracket in brackets:
        if bracket == '<':
            count += 1
        else:
            count -= 1
        if count < 0:
            return False
    return True
