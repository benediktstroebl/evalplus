

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
    stack = []
    for bracket in brackets:
        if bracket == ">":
            if stack:
                if stack[-1] == "<":
                    stack.pop()
                else:
                    return False
            else:
                return False
        else:
            stack.append(bracket)

    return True if not stack else False
