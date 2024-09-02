

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
    assert brackets[0] == "<" and brackets[-1] == ">"
    closing_brackets = {">", "<"}
    opening_brackets = {"(", "[", "{"}
    opening_brackets_set = set(opening_brackets)
    if not brackets[1:-1] in opening_brackets_set:
        return False
    return all(c in closing_brackets for c in brackets[1:-1
