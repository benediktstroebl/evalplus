

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
    brackets_dict = {
        "<": ">",
        ">": "<"
    }
    bracket_stack = []

    for bracket in brackets:
        if bracket in brackets_dict:
            bracket_stack.append(brackets_dict[bracket])
        else:
            if len(bracket_stack) == 0:
                return False
            if bracket_stack.pop() != bracket:
                return False

    return len(bracket_stack) == 0

