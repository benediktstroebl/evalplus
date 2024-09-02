

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
    opening_brackets = []
    for i in range(len(brackets)):
        if brackets[i] == "<":
            opening_brackets.append(brackets[i])
        elif brackets[i] == ">":
            if len(opening_brackets) == 0:
                return False
            opening_brackets.pop()

    return len(opening_brackets) ==
