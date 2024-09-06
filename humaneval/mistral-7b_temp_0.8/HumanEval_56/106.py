

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
        ">": "<",
    }

    current_bracket = None

    for bracket in brackets:
        if bracket == brackets_dict[current_bracket]:
            current_bracket = None
        elif brackets_dict.get(bracket, None) is not None:
            current_bracket = bracket
        else:
            return False

    if current_bracket is not None:
        return False

    return True

