

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

    bracketing_pairs = []

    for char in brackets:
        if char == "(":
            bracketing_pairs.append(char)
        elif char == ")":
            if len(bracketing_pairs) == 0:
                return False
            else:
                bracketing_pairs.pop()

    return len(bracketing_pairs) == 0
