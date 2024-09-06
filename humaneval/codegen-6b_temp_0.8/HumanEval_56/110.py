

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
    if not isinstance(brackets, str):
        return False
    if len(brackets) == 0:
        return True
    if len(brackets) % 2 != 0:
        return False
    char_lst = []
    for char in brackets:
        if char == "<":
            char_lst.append(">")
        elif char == ">":
            if len(char_lst) == 0:
                return False
            else:
                char_lst.pop()
    return len(char_lst) == 0

