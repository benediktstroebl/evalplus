

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
    result = True
    brackets = list(brackets)

    while brackets:
        current = brackets.pop(0)

        if current == "<":
            if brackets and brackets[0] == ">":
                brackets.pop(0)
        elif current == ">":
            if not brackets:
                return False
            if brackets[0] == "<":
                brackets.pop(0)
        else:
            return False

    return
