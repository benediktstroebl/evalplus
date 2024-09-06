

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
    """
    # Wrong answer:
    # if brackets == '':
    #     return True
    # if brackets[0] == '>':
    #     return False
    # return correct_bracketing(brackets[1:])
    """
    count = 0
    for b in brackets:
        if b == '<':
            count += 1
        else:
            count -= 1
            if count < 0:
                return False
    return count == 0
