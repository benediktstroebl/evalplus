

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
    brackets = brackets[:]
    if len(brackets) == 0:
        return True
    elif len(brackets) % 2 != 0:
        return False
    else:
        return is_correct(brackets[:len(brackets)//2]) and \
            is_correct(brackets[len(brackets)//2:])
