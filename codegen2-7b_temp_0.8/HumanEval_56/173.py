

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
    opening_brackets = "([{"
    closing_brackets = ")]}"

    opening_indices = [i for i, c in enumerate(brackets) if c in opening_brackets]
    closing_indices = [i for i, c in enumerate(brackets) if c in closing_brackets]

    return all(opening_indices[i + 1] == closing_indices[i] for i in range(len(closing_indices) -
