

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
    if len(brackets) % 2 != 0:
        return False
    opening_brackets = set("{[<")
    closing_brackets = set(">]}")
    if not set(brackets).issubset(opening_brackets) and not set(brackets).issubset(closing_brackets):
        return False
    opening_brackets_counter = 0
    closing_brackets_counter = 0
    for bracket in brackets:
        if bracket in opening_brackets:
            opening_brackets_counter += 1
        elif bracket in closing_brackets:
            closing_brackets_counter += 1
    return opening_brackets_counter == closing_brackets_counter

