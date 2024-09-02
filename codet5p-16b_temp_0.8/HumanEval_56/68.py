

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

    brackets = [char for char in brackets]
    if len(brackets) % 2:
        return False

    left_brackets = [char for char in brackets if char == "<"]
    if not left_brackets:
        return False

    left_brackets = left_brackets[:-1]
    right_brackets = [char for char in brackets if char == ">"]
    right_brackets = right_brackets[1:]
    right_brackets.reverse()

    if left_brackets[-1] + right_brackets[0]!= "<>":
        return False

    return correct_bracketing(">" + right_brackets[1:] + "<" + left_brackets[:-1])
