

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
    open_stack = []
    for character in brackets:
        if character == "<":
            open_stack.append(character)
        elif character == ">":
            if len(open_stack) == 0:
                return False
            top = open_stack.pop()
            if top != "<":
                return False
    return len(open_stack) == 0
