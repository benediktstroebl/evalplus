

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
    S = ArrayStack()
    for i in range(len(brackets)):
        if brackets[i] == "(":
            S.push("(")
        else:
            if S.is_empty():
                return False
            else:
                S.pop()
    return S.is_empty()
