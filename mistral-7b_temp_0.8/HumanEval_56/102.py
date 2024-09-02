

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
    # if there are not enough closing brackets
    if len(brackets_list) % 2 != 0:
        return False

    for idx in range(0, len(brackets_list), 2):
        if brackets_list[idx] == "<" and brackets_list[idx+1] != ">":
            return False
        elif brackets_list[idx] == ">" and brackets_list[idx+1] != "<":
            return False
    return True

