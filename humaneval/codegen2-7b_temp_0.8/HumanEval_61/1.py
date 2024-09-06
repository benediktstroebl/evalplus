

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
    assert len(brackets) >= 2, "Need at least two '('"

    bracket_stack = []
    for c in brackets:
        if c == "(":
            bracket_stack.append(c)
        else:
            assert len(bracket_stack) >= 1, "Unmatched '('"
            bracket_stack.pop()

    return len(bracket_stack) ==
