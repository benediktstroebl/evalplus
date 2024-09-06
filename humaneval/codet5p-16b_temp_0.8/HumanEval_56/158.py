

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

    brackets_stack = []
    for bracket in brackets:
        if bracket == "<":
            brackets_stack.append(bracket)
        elif bracket == ">":
            if not brackets_stack:
                return False
            elif brackets_stack[-1] == "<":
                brackets_stack.pop()
            else:
                return False
    if not brackets_stack:
        return True
    return False

