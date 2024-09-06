

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
    if len(brackets) % 2 == 1:
        return False
    open_brackets = [brackets[0]]
    for i in range(len(brackets)):
        if brackets[i] == "<":
            if brackets[i+1]!= ">":
                return False
        elif brackets[i] == ">":
            open_brackets.pop()
    return len(open_brackets) ==
