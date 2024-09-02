

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
    # Your code goes here...
    if len(brackets) == 0:
        return True
    elif brackets[0] == '<' and brackets[-1] == '>':
        return correct_bracketing(brackets[1:-1])
    elif brackets[0] == '<' and brackets[-1] == '>' and len(brackets) > 2:
        return correct_bracketing(brackets[1:-1])
    elif brackets[0] == '>' and brackets[-1] == '<':
        return correct_bracketing(brackets[1:-1])
    elif brackets[0] == '>' and brackets[-1] == '<' and len(brackets) > 2:
        return correct_bracketing(brackets[1:-1])
    else:
        return False

