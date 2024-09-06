

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
    open_brackets = find_open_brackets(brackets)
    close_brackets = find_close_brackets(brackets)
    if len(open_brackets)!= len(close_brackets):
        return False
    if len(open_brackets) == 0:
        return True
    for open_bracket, close_bracket in zip(open_brackets, close_brackets):
        if open_bracket!= close_bracket:
            return
