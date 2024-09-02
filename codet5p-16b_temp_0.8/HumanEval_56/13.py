

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

    brackets = list(brackets)
    opening_brackets = [">", "<<", "[", "]"]
    closing_brackets = ["><", ">>", "}", "]"]
    if any(bracket not in opening_brackets + closing_brackets for bracket in brackets):
        return False
    if len(brackets) % 2 == 1:
        return False
    stack = []
    for bracket in brackets:
        if bracket in opening_brackets:
            stack.append(bracket)
        elif bracket in closing_brackets:
            if not stack:
                return False
            top = stack.pop()
            if top!= opening_brackets.index(bracket):
                return False
    return not stack
