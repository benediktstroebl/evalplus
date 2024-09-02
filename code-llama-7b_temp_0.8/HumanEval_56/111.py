

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

    # keep track of how many opening brackets we have seen
    open_brackets = 0

    # for each character in brackets, keep track of how many
    # opening brackets we have seen. If the next character is
    # a closing bracket, then check that we have seen the same
    # number of opening brackets
    for char in brackets:
        if char == "<":
            open_brackets += 1
        elif char == ">":
            open_brackets -= 1
            if open_brackets < 0:
                return False

    return open_brackets == 0

