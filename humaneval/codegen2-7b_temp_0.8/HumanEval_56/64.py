

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
    closing_brackets = {'>': '<', '<': '>'}
    stack = []
    for char in brackets:
        if char in closing_brackets:
            stack.append(char)
        else:
            if len(stack) == 0:
                return False
            if stack.pop()!= closing_brackets[char]:
                return False
    if len(stack) > 0:
        return False
    return
