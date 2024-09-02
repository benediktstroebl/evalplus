

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
    bracket_count = 0
    for char in brackets:
        if char in bracket_dict.keys():
            bracket_count += 1
        elif char in bracket_dict.values():
            bracket_count -= 1

    if bracket_count != 0:
        return False
    else:
        return True

