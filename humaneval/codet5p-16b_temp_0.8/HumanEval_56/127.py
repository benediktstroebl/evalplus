

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

    opening_brackets = set()
    for character in brackets:
        if character == "<":
            opening_brackets.add(character)
        else:
            if not opening_brackets:
                return False
            opening_brackets.remove(character)

    return not opening_brackets

