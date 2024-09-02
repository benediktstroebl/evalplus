

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

    brackets = brackets.strip()
    open_brackets = "<"
    close_brackets = ">"
    result = True
    for char in brackets:
        if char in open_brackets:
            open_brackets = open_brackets.replace(char, "")
        if char in close_brackets:
            close_brackets = close_brackets.replace(char, "")

    if open_brackets != "":
        result = False
    if close_brackets != "":
        result = False

    return result

