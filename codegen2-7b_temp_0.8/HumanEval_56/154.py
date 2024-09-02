

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
    brackets = brackets.replace("<", "(").replace(">", ")")
    return all(b == brackets[brackets.index(c)+1] for c, b in zip(brackets, brackets[1:]))

