

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
    bracket_pair_dict = {
        "<": ">",
        ">": "<"
    }
    stack = []

    for i in brackets:
        if i in bracket_pair_dict.values():
            stack.append(i)
        elif i == stack.pop():
            continue
        else:
            return False

    return len(stack) == 0
