

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
    if brackets == "":
        return True
    opening = brackets[0]
    stack = []
    for c in brackets[1:]:
        if c == opening:
            stack.append(c)
        elif len(stack) > 0 and stack[-1] == opening:
            stack.pop()
        else:
            return False
    return len(stack) == 0
