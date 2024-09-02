

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
    stack = []
    stack_index = []
    for i in range(len(brackets)):
        if brackets[i] == "<":
            stack_index.append(i)
        elif brackets[i] == ">":
            if len(stack_index) == 0:
                return False
            else:
                stack_index.pop()

    if len(stack_index) == 0:
        return True
    else:
        return False

