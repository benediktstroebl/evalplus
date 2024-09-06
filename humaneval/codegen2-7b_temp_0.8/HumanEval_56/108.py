

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
    if len(brackets) % 2:
        return False
    stack = []
    for index in range(0, len(brackets), 2):
        if brackets[index] == '<':
            stack.append(brackets[index + 1])
        else:
            if stack:
                if stack.pop()!= brackets[index]:
                    return False
    return len(stack) == 0
