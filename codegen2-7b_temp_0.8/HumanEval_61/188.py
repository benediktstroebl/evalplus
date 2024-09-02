

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
    opening_brackets = ["(", "[", "{", "<"]
    closing_brackets = [")", "]", "}", ">"]

    for pair in opening_brackets + closing_brackets:
        if pair not in brackets:
            return False

    return True
