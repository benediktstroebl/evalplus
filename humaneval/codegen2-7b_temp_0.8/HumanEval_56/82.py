

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
    opening_brackets = "<{[("
    closing_brackets = "}]})>"
    stack = []
    for bracket in brackets:
        if bracket in opening_brackets:
            stack.append(bracket)
        elif len(stack) == 0 or opening_brackets.index(stack[-1])!= closing_brackets.index(bracket):
            return False
        else:
            stack.pop()
    return len(stack)
