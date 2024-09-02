

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
    bracket_stack = []
    for i in range(len(brackets)):
        if brackets[i] == "<":
            bracket_stack.append(">")
        elif brackets[i] == ">":
            if bracket_stack:
                bracket_stack.pop()
            else:
                return False
    return len(bracket_stack) == 0
