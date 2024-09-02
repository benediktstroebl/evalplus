

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

    opening_brackets = []
    for i in range(len(brackets)):
        if brackets[i] == "<":
            opening_brackets.append(i)
        if brackets[i] == ">":
            if opening_brackets:
                opening_brackets.pop()
            else:
                return False
    return not opening_brackets




