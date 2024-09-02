

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

    # Hint: Use a stack.
    stack = []
    for i in range(0,len(brackets)):
        if brackets[i] == ">":
            if not stack:
                return False
            else:
                stack.pop()
        else:
            stack.append(brackets[i])
    if stack:
        return False
    return True

