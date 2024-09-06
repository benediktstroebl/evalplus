

def correct_bracketing(brackets: str):
    """ brackets is a string of "(" and ")".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("(")
    False
    >>> correct_bracketing("()")
    True
    >>> correct_bracketing("(()())")
    True
    >>> correct_bracketing(")(()")
    False
    """
    correct = True
    stack = []
    for x in brackets:
        if x == "(":
            stack.append(x)
        else:
            if not stack:
                correct = False
                break
            else:
                bracket = stack.pop()
                if bracket != "(":
                    correct = False
                    break
    if correct and not stack:
        return True
    else:
        return False

import sys