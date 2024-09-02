

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
    # find the number of open brackets
    num_open = brackets.count("<")

    # find the number of close brackets
    num_close = brackets.count(">")

    # if the numbers are equal, the string has balanced brackets
    return num_open == num_close
