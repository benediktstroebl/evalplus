

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

    assert len(brackets) % 2 == 0
    stack = []
    for i in range(len(brackets)):
        if brackets[i] == "<":
            stack.append(i)
        elif brackets[i] == ">":
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    return len(stack) == 0

