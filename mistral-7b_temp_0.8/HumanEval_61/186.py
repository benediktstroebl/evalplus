

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
    if len(brackets) % 2 != 0:
        return False

    bracket_list = list(brackets)
    opening_bracket = "("
    closing_bracket = ")"
    closing_bracket_index = bracket_list.index(closing_bracket)

    if opening_bracket in bracket_list and closing_bracket in bracket_list:
        while opening_bracket in bracket_list:
            if closing_bracket_index == -1:
                return False
            elif opening_bracket == bracket_list[closing_bracket_index - 1]:
                bracket_list.pop(closing_bracket_index - 1)
                bracket_list.pop(closing_bracket_index)
            closing_bracket_index = bracket_list.index(closing_bracket)
        return True
    return False
