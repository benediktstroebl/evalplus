

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
    opening = "<"
    closing = ">"

    # count the number of opening brackets
    count = brackets.count(opening)
    # count the number of closing brackets
    count_closing = brackets.count(closing)

    return (count == count_closing)
