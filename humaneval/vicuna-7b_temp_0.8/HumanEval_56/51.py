

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
    opening_brackets = set(brackets.split(" "))
    closing_brackets = set(brackets.split(" "))

    for opening in opening_brackets:
        for i in range(len(opening_brackets) - 1):
            if opening != opening_brackets[i + 1]:
                return False

    return True
