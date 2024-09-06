

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
    # TODO: implement this function.

    if len(brackets) == 0:
        return True

    counter = 0
    for i in brackets:
        if i == '<':
            counter += 1
        elif i == '>':
            counter -= 1

    return counter == 0

