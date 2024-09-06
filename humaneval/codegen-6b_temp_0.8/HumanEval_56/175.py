

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
    i = 0
    bracket_stack = []

    while i < len(brackets):
        if brackets[i] == "<":
            bracket_stack.append("<")
        elif brackets[i] == ">":
            if len(bracket_stack) == 0 or bracket_stack.pop() != "<":
                return False
        i += 1

    return len(bracket_stack) == 0


