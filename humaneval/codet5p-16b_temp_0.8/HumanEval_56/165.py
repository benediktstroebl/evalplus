

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

    open_brackets = "("
    closed_brackets = ")"
    close_brackets = ">"
    stack = []

    for b in brackets:
        if b in open_brackets:
            stack.append(b)
        elif b in closed_brackets:
            if not stack:
                return False
            elif stack[-1] == ">":
                stack.pop()
            else:
                return False
    if not stack:
        return True
    else:
        return False
