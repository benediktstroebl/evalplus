

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
    num_open_brackets = 0
    for char in brackets:
        if char == '(':
            num_open_brackets += 1
        elif char == ')':
            num_open_brackets -= 1
        if num_open_brackets < 0:
            return False
    return num_open_brackets == 0

