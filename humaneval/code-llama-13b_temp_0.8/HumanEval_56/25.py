

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
    # for i in range(len(brackets)):
    #     if brackets[i] == "<":
    #         if not any(i < j < len(brackets) and brackets[j] == ">"
    #                    for j in range(i, len(brackets))):
    #             return False
    # return True

    stack = []
    for i in brackets:
        if i == "<":
            stack.append(i)
        else:
            if not stack:
                return False
            if stack.pop() != "<":
                return False
    return not stack

