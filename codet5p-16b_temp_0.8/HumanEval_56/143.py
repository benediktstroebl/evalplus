

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
    brackets_stack = []

    for bracket in brackets_list:
        if bracket == "<":
            brackets_stack.append(bracket)
        else:
            if brackets_stack:
                brackets_stack.pop()
            else:
                return False
    return brackets_stack == []

