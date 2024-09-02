

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
    bracket_dict = {"(":")", ")":"("}

    if len(brackets)%2 != 0:
        return False

    stack = []

    for c in brackets:
        if c in bracket_dict.keys():
            stack.append(c)
        else:
            if not stack:
                return False
            elif stack.pop() != bracket_dict[c]:
                return False

    return not stack


