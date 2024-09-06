

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
    # my solution
    # TODO: your code here
    stack = []
    for bracket in brackets:
        if bracket == "(":
            stack.append("(")
        elif bracket == ")":
            if len(stack) > 0:
                stack.pop()
            else:
                return False
    return stack == []

    # another solution
    # while brackets:
    #     if brackets[0] == "(":
    #         brackets = brackets[1:]
    #     elif brackets[0] == ")":
    #         if brackets[0] == "(":
    #             brackets = brackets[1:]
    #         else:
    #             return False
    #     else:
    #         return False
    # return True

    # third solution
    # stack = []
    # for b in brackets:
    #     if b == "(":
    #         stack.append(b)
    #     else:
    #         if len
