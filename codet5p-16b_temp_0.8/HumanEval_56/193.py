

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

    correct_brackets = set(brackets)
    brackets = list(brackets)
    while brackets:
        bracket = brackets.pop()
        if bracket == ">":
            if brackets and brackets[-1] == "<":
                brackets.pop()
            else:
                return False
        elif bracket == "<":
            if brackets and brackets[-1] == ">":
                brackets.pop()
            else:
                return False
        else:
            return False
    return True

