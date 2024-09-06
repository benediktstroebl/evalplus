

def correct_bracketing(brackets: str):
    """ brackets is a string of "<" and ">".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("<")
    False
    >>> correct_bracketing("<>")
    True
    >>> correct_bracketing("<<><>>")
    True
    >>> correct_bracketing("><<>")
    False
    """
    if len(brackets) == 0:
        return True
    if brackets[0] == ">":
        return False
    else:
        return correct_bracketing(brackets[1:])

    # If your code passes the tests but runs too slowly, consider using this code.
    # It runs faster, but it produces the wrong answer if there are more than
    # 1000000000 closing brackets.
    # if brackets[0] == ">":
    #     return False
    # if brackets[-1] == "<":
    #     return False
    # return correct_bracketing(brackets[1:-1])
