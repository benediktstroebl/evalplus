

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
    opening_brackets = set(brackets.strip("()").split(" "))
    closing_brackets = set(brackets.strip("()").split(" "))
    for opening_bracket in opening_brackets:
        for i in range(1, len(opening_bracket)):
            if not closing_brackets.issubset(opening_bracket[i:]) or opening_bracket[i] != "(":
                return False
    return True
