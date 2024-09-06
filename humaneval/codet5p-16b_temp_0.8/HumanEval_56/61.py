

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

    brackets = brackets.replace(' ', '')
    bracket_stack = []
    for bracket in brackets:
        if bracket == '<':
            bracket_stack.append('<')
        elif bracket == '>':
            if bracket_stack and bracket_stack[-1] == '<':
                bracket_stack.pop()
            else:
                return False
    return not bracket_stack
