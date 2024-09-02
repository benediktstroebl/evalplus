

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
    opening = "(){}[]<>"
    stack = []
    for bracket in brackets:
        if bracket in opening:
            stack.append(bracket)
        else:
            if stack and stack[-1] == bracket[0]:
                stack.pop()
            else:
                return False
    return not stack

