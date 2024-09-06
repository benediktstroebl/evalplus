

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

    # Solution 1
    # return len(brackets) == brackets.count("<")

    # Solution 2
    # return len(brackets) == brackets.count("<") and len(brackets) == brackets.count(">")

    # Solution 3
    # return len(brackets) == brackets.count("<") and len(brackets) == brackets.count(">") and \
    #        brackets.count("<") == brackets.count(">")

    # Solution 4
    # return brackets.count("<") == brackets.count(">")

    # Solution 5
    # return brackets.count("<") == brackets.count(">") and \
    #        not "<" in brackets.replace("<", "") and \
    #        not ">" in brackets.replace(">", "")

    # Solution 6
    # return brackets.count("<") == brackets.count(">") and \
    #        not "><" in brackets and \
