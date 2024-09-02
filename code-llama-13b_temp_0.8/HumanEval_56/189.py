

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
    assert type(brackets) == str, repr(brackets) + ' is not a string.'
    assert '>' not in brackets and '<' in brackets, repr(brackets) + ' is not valid.'
    stack = []
    for bracket in brackets:
        if bracket == '<':
            stack.append(bracket)
        else:
            if not stack:
                return False
            else:
                stack.pop()
    return not stack

