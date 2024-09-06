

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
    bracket_map = {">": "<", "<": ">"}
    open_brackets = []
    for c in brackets:
        if c == "<":
            open_brackets.append(c)
        elif c == ">":
            if len(open_brackets) == 0:
                return False
            else:
                open_brackets.pop()

    if len(open_brackets) != 0:
        return False

    return True

