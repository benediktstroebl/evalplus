

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
    #get number of opening brackets
    num_open = brackets.count("<")
    #get number of closing brackets
    num_close = brackets.count(">")

    if num_open > num_close:
        return False
    else:
        return True

