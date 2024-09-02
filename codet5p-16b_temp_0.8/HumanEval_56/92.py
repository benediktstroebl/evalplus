

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

    if len(brackets) % 2:
        return False
    stack = []
    for bracket in brackets:
        if bracket == ">" and stack and stack[-1] == "<":
            stack.pop()
        else:
            stack.append(bracket)
    return not stack

