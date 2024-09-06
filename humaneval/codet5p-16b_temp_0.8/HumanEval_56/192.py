

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

    brackets_map = {"<": ">", ">": "<"}

    opened_brackets = []

    for bracket in brackets:
        if bracket == "<":
            opened_brackets.append(bracket)
        elif bracket == ">":
            if len(opened_brackets) == 0:
                return False
            opened_brackets.pop()

    return len(opened_brackets) == 0

