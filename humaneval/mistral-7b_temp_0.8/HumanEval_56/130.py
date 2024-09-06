

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
    brackets = brackets.split("")
    for bracket in brackets:
        if bracket == "<":
            bracket_stack.append("<")
        else:
            if bracket_stack:
                bracket_stack.pop()
            else:
                return False
    return len(bracket_stack) == 0

