

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
    for opening_brace in brackets:
        if not brackets.find(opening_brace) % 2 == 0:
            return False
    return True

@pytest.mark.parametrize("brackets", [("("), ("["), ("]")], indirect=True)
