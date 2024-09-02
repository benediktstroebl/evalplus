

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
    brackets = brackets.replace("><", "")
    if len(brackets) % 2 != 0:
        return False
    stack = []
    for bracket in brackets:
        if bracket == "<":
            stack.append(bracket)
        else:
            if not stack:
                return False
            stack.pop()
    return True



