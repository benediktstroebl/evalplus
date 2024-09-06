

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
    bracket_dict = {"<": ">", ">": "<"}
    stack = []
    for bracket in brackets:
        if bracket in bracket_dict:
            stack.append(bracket)
        elif bracket == bracket_dict[stack.pop()]:
            continue
        else:
            return False
    if len(stack) > 0:
        return False
    return True

