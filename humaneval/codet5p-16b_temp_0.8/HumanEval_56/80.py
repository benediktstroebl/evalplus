

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

    bracket_stack = []
    for i in brackets:
        if i == "<":
            bracket_stack.append(i)
        elif i == ">":
            if len(bracket_stack) == 0:
                return False
            if bracket_stack[-1] == "<":
                bracket_stack.pop()
            else:
                return False
    if len(bracket_stack)!= 0:
        return False
    return True
