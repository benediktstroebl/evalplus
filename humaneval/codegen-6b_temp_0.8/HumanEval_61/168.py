

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
    assert type(brackets) == str, "brackets must be a string"
    assert len(brackets) > 0, "brackets cannot be empty"
    assert all(char in "()" for char in brackets), "brackets must be balanced"
    correct_brackets = 0
    for bracket in brackets:
        if bracket == "(":
            correct_brackets += 1
        elif bracket == ")":
            correct_brackets -= 1
        if correct_brackets < 0:
            return False
    return correct_brackets == 0

