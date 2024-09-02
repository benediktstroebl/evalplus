

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
    closing = []
    for i in range(len(brackets)):
        if brackets[i] == ">" and closing == []:
            return False
        elif brackets[i] == "<":
            closing.append(brackets[i])

    return len(closing) == 0

