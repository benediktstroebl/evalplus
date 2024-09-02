

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
    if len(brackets) % 2 != 0:
        return False
    counter = 0
    for char in brackets:
        if char == '(':
            counter += 1
        elif char == ')':
            counter -= 1
        if counter < 0:
            return False
    return counter == 0

