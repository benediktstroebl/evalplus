

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
    i = 0
    stack = []
    while i < len(brackets):
        if brackets[i] == '<':
            stack.append(i)
            i += 1
        elif brackets[i] == '>':
            if len(stack) == 0:
                return False
            stack.pop()
            i += 1
        else:
            i += 1
    if len(stack) == 0:
        return True
    else:
        return False

