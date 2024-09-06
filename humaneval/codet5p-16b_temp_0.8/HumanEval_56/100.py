

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
    brackets.append('<')
    brackets.append('>')
    stack = []
    for bracket in brackets:
        if bracket == '<':
            stack.append('<')
        elif bracket == '>':
            if stack == []:
                return False
            stack.pop()
    return stack == []

