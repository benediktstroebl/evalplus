

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
    cnt = 0
    bracket_list = list(brackets)
    if len(brackets) % 2 != 0:
        return False
    for b in bracket_list:
        if b == '<':
            cnt += 1
        elif b == '>':
            cnt -= 1
            if cnt < 0:
                return False
    if cnt == 0:
        return True
    else:
        return False

