

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
    if not brackets:
        return True

    unmatched_brackets = []

    for bracket in brackets:
        if bracket == '(':
            unmatched_brackets.append(bracket)
        elif bracket == ')':
            if unmatched_brackets:
                unmatched_brackets.pop()
            else:
                unmatched_brackets.append(bracket)

    return not unmatched_brackets
