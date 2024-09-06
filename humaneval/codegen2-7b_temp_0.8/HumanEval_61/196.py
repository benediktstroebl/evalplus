

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
    if len(brackets) % 2!= 0:
        return False
    opening = []
    closing = []
    for i, character in enumerate(brackets):
        if character == '(':
            opening.append(i)
        elif character == ')':
            if len(opening) == 0:
                return False
            closing.append(opening.pop())
    return len(opening) == 0
