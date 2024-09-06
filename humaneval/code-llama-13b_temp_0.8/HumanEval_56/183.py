

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
    if not len(brackets):
        return True
    else:
        if len(brackets) == 1:
            return False
        if brackets[0] == ">":
            return False
        if brackets[0] == "<":
            stack = [brackets[0]]
        else:
            return False
        for char in brackets[1:]:
            if char == "<":
                stack.append(char)
            elif char == ">":
                if len(stack) == 0:
                    return False
                else:
                    stack.pop()
        if len(stack) == 0:
            return True
        else:
            return False

