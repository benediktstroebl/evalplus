

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
    opening_bracket_list = [">", "<"]
    return all(opening_bracket_list.count(bracket) == closing_bracket_list.count(bracket)
               for bracket, closing_bracket in zip(brackets, brackets[1:] + brackets[:1]))
