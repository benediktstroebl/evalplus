

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
    closing_brackets = []
    for bracket in brackets:
        if bracket == "(":
            closing_brackets.append(")")
        elif len(closing_brackets) > 0:
            last_open_bracket = closing_brackets.pop()
            if last_open_bracket != bracket:
                return False

    return (len(closing_brackets) == 0)

