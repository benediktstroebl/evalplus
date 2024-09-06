

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

    # your code here
    # count opening and closing brackets
    # if opening bracket count is less than closing bracket count, return False
    # if opening bracket count is greater than closing bracket count, return False
    # if opening bracket count is equal to closing bracket count, return True
    openBrackets = 0
    closedBrackets = 0
    for c in brackets:
        if c == "<":
            openBrackets += 1
        elif c == ">":
            closedBrackets += 1
        else:
            raise Exception("invalid character in brackets")

    return openBrackets == closedBrackets

