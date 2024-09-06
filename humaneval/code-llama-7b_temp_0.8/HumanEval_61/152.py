

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
    # Returns whether all the opening brackets have corresponding closing brackets
    # and all the closing brackets have corresponding opening brackets
    opening = '('
    closing = ')'
    open_count = 0
    closing_count = 0
    for char in brackets:
        if char == opening:
            open_count += 1
        elif char == closing:
            closing_count += 1
            if open_count <= 0:
                return False
    return open_count == closing_count

