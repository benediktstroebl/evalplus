

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
    for character in brackets:
        if character == ">":
            if len(stack) == 0 or stack.pop() != "<":
                return False
        elif character == "<":
            stack.append(character)

    return len(stack) == 0

import doctest