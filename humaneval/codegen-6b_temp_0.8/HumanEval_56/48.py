

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
    if not brackets:
        return True

    if len(brackets) % 2 == 0:
        return False

    stack = []

    for bracket in brackets:
        if bracket == ">" and not stack or bracket == "<" and stack.pop() != ">":
            return False
        stack.append(bracket)

    return not stack

