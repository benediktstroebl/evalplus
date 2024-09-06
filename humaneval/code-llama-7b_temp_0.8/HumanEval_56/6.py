

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
    # BEGIN PROBLEM 1
    brackets_count = 0
    for bracket in brackets:
        if bracket == "<":
            brackets_count += 1
        else:
            if brackets_count > 0:
                brackets_count -= 1
            else:
                return False
    return brackets_count == 0
    # END PROBLEM 1

