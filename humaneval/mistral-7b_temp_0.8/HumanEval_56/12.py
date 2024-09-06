

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

    # if brackets.count("<") != brackets.count(">"):
    #     return False

    # if brackets.count("<") % 2 != 0:
    #     return False

    # if brackets.count(">") % 2 != 0:
    #     return False

    # while "<" in brackets:
    #     brackets = brackets.replace("<", "", 1)
    #     brackets = brackets.replace(">", "", 1)

    # while ">" in brackets:
    #     brackets = brackets.replace(">", "", 1)
    #     brackets = brackets.replace("<", "", 1)

    # return len(brackets) == 0

    # return brackets.replace("<", "").replace(">", "") == ""

    # return brackets.count("<") == brackets.count(">")

    if brackets.count("<") % 2 != 0 or brackets.count(">") %
