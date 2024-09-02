

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

    closing_brackets = {}

    for i in range(len(brackets)):
        if brackets[i] == "<":
            closing_brackets[i] = ">"
        elif brackets[i] == ">":
            closing_brackets[i] = "<"

    for i in range(len(brackets) // 2):
        if closing_brackets[i] != brackets[len(brackets) - i - 1]:
            return False

    return True

