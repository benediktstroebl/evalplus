

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

    open_brackets = []
    for i in range(len(brackets)):
        if brackets[i] == '<':
            open_brackets.append(i)
        elif brackets[i] == '>':
            if len(open_brackets) == 0:
                return False
            else:
                open_brackets.pop()

    return True if len(open_brackets) == 0 else False

