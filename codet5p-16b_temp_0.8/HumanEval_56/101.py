

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

    bracketing = brackets.replace("<", "(").replace(">", ")")
    bracket_list = bracketing.split("(")
    if bracket_list[0]!= "":
        return False
    for bracket in bracket_list[1:]:
        if bracket.count(")")!= bracket.count("("):
            return False
    return True

