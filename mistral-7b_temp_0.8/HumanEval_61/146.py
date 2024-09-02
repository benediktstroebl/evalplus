

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
    # open_brackets_stack = []
    # for bracket in brackets:
    #     if bracket == "(":
    #         open_brackets_stack.append(bracket)
    #     elif bracket == ")":
    #         if len(open_brackets_stack) > 0:
    #             open_brackets_stack.pop()
    #         else:
    #             return False
    # return len(open_brackets_stack) == 0

    # close_brackets = []
    # for bracket in brackets:
    #     if bracket == "(":
    #         close_brackets.append(")")
    #     else:
    #         close_brackets.append("(")
    # return brackets == close_brackets

    # if len(brackets) % 2 == 1:
    #     return False
    # open_brackets_stack = 0
    # for bracket in brackets:
    #     if br
