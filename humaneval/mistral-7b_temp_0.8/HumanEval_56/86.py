

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
    brackets_list = list(brackets)
    brackets_list = brackets_list[::-1]
    brackets_list.append("<")
    opened = 0
    for i in brackets_list:
        if i == ">":
            opened += 1
        if i == "<":
            opened -= 1
        if opened < 0:
            return False
    return opened == 0

