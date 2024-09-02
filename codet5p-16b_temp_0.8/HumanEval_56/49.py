

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
    for bracket in brackets:
        if bracket == ">" and len(stack) == 0:
            return False
        elif bracket == ">" and len(stack) > 0:
            stack.pop()
        elif bracket == "<" and len(stack) == 0:
            stack.append(bracket)
        elif bracket == "<" and len(stack) > 0:
            stack.pop()

    return len(stack) == 0

