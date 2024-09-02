

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
    count_brackets = 0
    count_brackets_open = 0
    count_brackets_close = 0
    for i in brackets:
        if i == "<":
            count_brackets_open += 1
        if i == ">":
            count_brackets_close += 1
            if count_brackets_open > 0:
                count_brackets_open -= 1
            else:
                count_brackets += 1
    return count_brackets == count_brackets_open

