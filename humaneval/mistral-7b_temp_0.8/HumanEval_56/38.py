

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
    for bracket in brackets:
        if bracket == "<" or bracket == ">":
            bracket_count += 1
            if bracket_dict[bracket] not in brackets:
                return False
        else:
            continue
    if bracket_count % 2 == 0:
        return True
    else:
        return False

