

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

    brackets = [brackets[0]]
    for b in brackets:
        if b == ">" and brackets and brackets[-1] == "<":
            brackets.pop()
        else:
            brackets.append(b)
    return len(brackets) == 1
