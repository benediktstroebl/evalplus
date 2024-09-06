

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
    # your code here
    # Need to handle corner cases where the string is empty or just one of the brackets.

    # solution for long strings
    # if len(brackets) % 2 != 0:
    #     return False
    # start = 0
    # end = len(brackets) - 1
    # while start < end:
    #     if brackets[start] == "(":
    #         if brackets[end] == ")":
    #             start += 1
    #             end -= 1
    #         else:
    #             return False
    #     else:
    #         return False
    # return True

    # solution for short strings
    # if brackets == "":
    #     return True
    # elif brackets[0] == "(" and brackets[-1] == ")":
    #     return True
    # else:
    #     return False

    # solution for both
    if brackets == "" or len(brackets) == 1:
        return True
