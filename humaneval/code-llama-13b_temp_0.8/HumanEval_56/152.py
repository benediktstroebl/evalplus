

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
    # is_balanced = True
    # for i in range(len(brackets)):
    #     if brackets[i] == "<":
    #         if is_balanced:
    #             is_balanced = False
    #         else:
    #             is_balanced = True
    #     else:
    #         if is_balanced:
    #             is_balanced = False
    #         else:
    #             is_balanced = True
    # return is_balanced
    # return ">" * brackets.count("<") == brackets
    return len(brackets) % 2 == 0

