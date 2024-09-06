

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
    opening = "<"
    closing = ">"
    brackets_stack = []
    for bracket in brackets:
        if bracket == opening:
            brackets_stack.append(bracket)
        elif bracket == closing:
            if not brackets_stack:
                return False
            elif brackets_stack[-1] == opening:
                brackets_stack.pop()
            else:
                return False
    return not brackets_stack

