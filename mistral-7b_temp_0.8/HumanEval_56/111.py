

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
    # OPEN BRACKETS: <
    # CLOSING BRACKETS: >

    # first, let's make sure we are only given "<" and ">"
    if len(brackets) != len(set(brackets)):
        return False

    opening_brackets = 0
    closing_brackets = 0

    for char in brackets:
        if char == '<':
            opening_brackets += 1
        elif char == '>':
            closing_brackets += 1

    return opening_brackets == closing_brackets

