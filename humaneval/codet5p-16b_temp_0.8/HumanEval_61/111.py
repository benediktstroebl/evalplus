

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

    if brackets == "":
        return True
    else:
        i = 0
        if brackets[i] == "(":
            i += 1
        else:
            return False
        while i < len(brackets):
            if brackets[i] == ")":
                i += 1
                if brackets[i] == "(":
                    i += 1
                    continue
                else:
                    return False
            else:
                return False
        return True

