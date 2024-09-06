

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
    if len(brackets) % 2 != 0:
        return False
    stack = []
    for i in range(0, len(brackets) - 1, 2):
        if brackets[i] == ">" and brackets[i + 1] == "<":
            stack.append(">")
        elif brackets[i] == "<" and brackets[i + 1] == ">":
            stack.pop()
        else:
            return False
    return not stack
