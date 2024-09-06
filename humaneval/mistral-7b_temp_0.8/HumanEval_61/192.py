

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

    #TODO
    #add a counter which counts the opening and closing brackets
    #if the number of opening brackets is not equal to the number of closing brackets, return false

    opening = 0
    closing = 0

    for i in brackets:
        if i == '(':
            opening += 1
        elif i == ')':
            closing += 1

        if opening != closing:
            return False

    return True
