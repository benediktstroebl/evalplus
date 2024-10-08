

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

    if brackets[0] not in "<>":
        return False

    stack = BracketStack(brackets[0])

    for bracket in brackets[1:]:
        if bracket == "<":
            stack.push(bracket)
        elif bracket == ">":
            if stack.is_empty():
                return False
            else:
                stack.pop()

    return stack.is_empty()
