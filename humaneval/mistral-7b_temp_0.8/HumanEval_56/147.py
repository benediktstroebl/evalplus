

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
    # BRUTE FORCE
    # count_open = 0
    # count_close = 0
    # for bracket in brackets:
    #     if bracket == "<":
    #         count_open += 1
    #     elif bracket == ">":
    #         count_close += 1
    #     else:
    #         raise ValueError("No brackets!")
    # if count_open == count_close:
    #     return True
    # else:
    #     return False

    # RECURSIVE SOLUTION
    # if len(brackets) == 0:
    #     return True
    # if brackets[0] == "<":
    #     if correct_bracketing(brackets[1:]):
    #         return True
    #     else:
    #         return False
    # elif brackets[0] == ">":
    #     if correct_bracketing(brackets[1:]):
    #         return True
    #     else:
    #         return
