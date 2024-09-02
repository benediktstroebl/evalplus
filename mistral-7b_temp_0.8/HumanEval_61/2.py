

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
    brackets = [b for b in brackets]
    opening_bracket = []
    closing_bracket = []
    i = 0
    while i < len(brackets):
        if brackets[i] == '(':
            opening_bracket.append(brackets[i])
            i += 1
        elif brackets[i] == ')':
            if len(opening_bracket) == 0:
                closing_bracket.append(brackets[i])
            else:
                opening_bracket.pop()
                i += 1
        i += 1

    if len(opening_bracket) == 0:
        return True
    else:
        return False

