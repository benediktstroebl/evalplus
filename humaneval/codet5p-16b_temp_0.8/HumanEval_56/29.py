

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

    brackets = iter(brackets)
    open_brackets = []
    for bracket in brackets:
        if bracket == '<':
            open_brackets.append(bracket)
        elif bracket == '>':
            try:
                if open_brackets[-1] == '<':
                    open_brackets.pop()
                else:
                    return False
            except IndexError:
                return False
        else:
            return False
    if open_brackets:
        return False
    return True

