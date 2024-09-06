

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
    opening_brackets = "<"
    closing_brackets = ">"
    brackets_list = list(brackets)
    opening_brackets_count = 0
    closing_brackets_count = 0
    while opening_brackets_count != closing_brackets_count:
        if opening_brackets in brackets_list:
            brackets_list.remove(opening_brackets)
            opening_brackets_count += 1
        elif closing_brackets in brackets_list:
            brackets_list.remove(closing_brackets)
            closing_brackets_count += 1
    if opening_brackets_count == closing_brackets_count:
        return True
    return False

