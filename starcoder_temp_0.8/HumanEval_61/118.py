

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
    n = len(brackets)
    opening_brackets = []
    for i in range(n):
        if brackets[i] == "(":
            opening_brackets.append(i)
        elif brackets[i] == ")":
            if opening_brackets == []:
                return False
            else:
                opening_brackets.pop()
    return opening_brackets == []

