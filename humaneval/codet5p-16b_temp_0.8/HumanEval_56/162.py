

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
    left_brackets = []
    for i in range(len(brackets)):
        if brackets[i] == "<":
            left_brackets.append(i)
        elif brackets[i] == ">":
            if len(left_brackets) == 0:
                return False
            else:
                left_brackets.pop()
    if len(left_brackets)!= 0:
        return False
    return True
