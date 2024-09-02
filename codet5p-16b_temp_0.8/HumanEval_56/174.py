

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

    brackets_list = brackets.split(">")
    if len(brackets_list) < 2:
        return True
    for bracket in brackets_list[:-1]:
        if bracket.count("<")!= bracket.count(">"):
            return False
    return correct_bracketing("".join(brackets_list[:-1]))

