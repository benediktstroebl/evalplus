

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

    # Using a list to hold the brackets that are opened, but not yet closed.
    # A new opening bracket will push a ">" onto the list.
    # A closing bracket will pop the most recently pushed ">" from the list.
    # If the list is ever empty, we have correctly bracketed the expression.
    stack = []
    for b in brackets:
        if b == "<":
            stack.append(">")
        elif b == ">" and stack:
            stack.pop()
        else:
            return False
    return not stack
