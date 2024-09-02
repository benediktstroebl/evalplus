

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
    counter = 0
    stack = []
    for bracket in brackets:
        if bracket == "(":
            stack.append(bracket)
            counter += 1
        else:
            if not stack:
                return False
            stack.pop()

    return counter == 0

