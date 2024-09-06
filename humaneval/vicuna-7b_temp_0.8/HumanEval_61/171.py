

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
    if any(not re.match(r"\w+", b) for b in brackets):
        return False
    return all(re.match(r"\w+", b) for b in brackets)

print(correct_bracketing("(()()))"))