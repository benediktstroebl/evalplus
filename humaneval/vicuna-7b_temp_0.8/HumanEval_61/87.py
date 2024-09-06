

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
    for bracket in brackets:
        if bracket not in ")\(", or not bracket in brackets:
            return False
    return True

print(correct_bracketing(")(()))") # should print True
print(correct_bracketing("(()") )
