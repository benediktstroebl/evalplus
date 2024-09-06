

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
    # assert type(brackets) == str
    if len(brackets) < 2:
        return True
    else:
        if brackets[0] == '<' and brackets[-1] == '>' or brackets[0] == '>' and brackets[-1] == '<':
            return correct_bracketing(brackets[1:-1])
        else:
            return False

