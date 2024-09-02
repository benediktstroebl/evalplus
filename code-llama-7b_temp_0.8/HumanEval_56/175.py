

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
    "*** YOUR CODE HERE ***"
    stack = []
    for i in range(len(brackets)):
        if brackets[i] == "<":
            stack.append(i)
        elif brackets[i] == ">" and len(stack) > 0:
            stack.pop()
            if len(stack) == 0:
                return False
    return len(stack) == 0

