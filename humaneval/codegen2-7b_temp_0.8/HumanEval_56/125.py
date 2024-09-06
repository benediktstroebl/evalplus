

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
    s = []
    for char in brackets:
        if char not in s and char!= ">":
            s.append(char)
        elif char == ">":
            s.pop()
    if not s:
        return True
    else:
        return False
