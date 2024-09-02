

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

    brackets = list(brackets)
    stack = []
    for b in brackets:
        if b == "<":
            stack.append(">")
        else:
            if stack:
                stack.pop()
            else:
                return False

    return not stack

