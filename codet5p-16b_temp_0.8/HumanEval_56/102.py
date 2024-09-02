

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

    assert len(brackets) % 2 == 0, f"{brackets} is a string of opening and closing brackets"

    open_brackets = set("<")
    close_brackets = set(">")

    open_bracket_counter = 0
    close_bracket_counter = 0

    for bracket in brackets:
        if bracket in open_brackets:
            open_bracket_counter += 1
        elif bracket in close_brackets:
            close_bracket_counter += 1

    if open_bracket_counter == close_bracket_counter:
        return True
    else:
        return False

