

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
    # if brackets.count("(") != brackets.count(")"):
    #     return False
    #
    # stack = []
    #
    # for i in brackets:
    #     if i == "(":
    #         stack.append(i)
    #     elif i == ")":
    #         if len(stack) > 0:
    #             stack.pop()
    #         else:
    #             return False
    # return True

    # stack = []
    #
    # for i in brackets:
    #     if i == "(":
    #         stack.append(i)
    #     elif i == ")":
    #         if len(stack) > 0:
    #             stack.pop()
    #         else:
    #             return False
    # return True

    # stack = []
    # for i in brackets:
    #     if i == '(':
    #         stack.append(i)
    #     elif i == ')':
    #         if not stack:
    #             return False
    #         stack.pop()
    # return not stack

    # stack = []
    # for i in brackets:
    #     if i == '(':
    #         stack.append(i)
    #     elif i == ')':
    #         if not stack:
    #             return False
    #         stack.pop()
    # return True

    # stack = []
    # for i in brackets:
    #     if i == "(":
    #         stack.append(i)
    #     elif i == ")":
    #         if stack:
    #             stack.pop()
    #         else:
    #             return False
    # return not stack

    stack = []
    for i in brackets:
        if i == "(":
            stack.append(i)
        elif i == ")":
            stack.pop()
    return not stack

