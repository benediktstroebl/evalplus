

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
    for i, bracket in enumerate(brackets):
        if bracket == "<":
            brackets_stack.append(i)
        if bracket == ">" and len(brackets_stack) > 0:
            brackets_stack.pop()
    return len(brackets_stack) == 0

