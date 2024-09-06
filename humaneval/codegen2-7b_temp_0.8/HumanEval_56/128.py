

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
    for b in brackets:
        if b == "<":
            if stack and stack[-1] == ">":
                stack.pop()
            else:
                stack.append(b)
        else:
            stack.append(b)
            if stack and stack[-1]!= "<" and stack[-1]!= ">":
                return False
    return
