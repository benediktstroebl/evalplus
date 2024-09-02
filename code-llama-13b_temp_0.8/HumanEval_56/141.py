

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

    # An empty string is balanced.
    if len(brackets) == 0:
        return True

    # The brackets are not balanced if the first character is a closing bracket.
    if brackets[0] == ">":
        return False

    # If the first character is an opening bracket,
    # then we can solve the problem by recurring on the rest of the string
    # and checking if the closing bracket is matched.
    # But we need to make sure that the closing bracket is indeed a closing bracket
    # and not another opening bracket.
    if len(brackets) > 1:
        closing_index = brackets.find(">")
        return brackets[closing_index:closing_index + 1] == ">" and correct_bracketing(
            brackets[closing_index + 1:]
        )

    return False

