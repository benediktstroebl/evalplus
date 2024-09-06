

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
    # Convert to a set of tuples
    brackets = set(brackets.split(" "))
    for i in range(len(brackets)):
        if i % 2 != 0:
            return False
        for j in range(i + 1, len(brackets)):
            if j % 2 != 0:
                return False
            if brackets[i] != brackets[j]:
                return False
    return True
