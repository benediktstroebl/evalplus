

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
    # 1. make a list of the positions of the opening and closing brackets
    open_brackets_positions = [pos for pos, bracket in enumerate(brackets) if bracket == "<"]
    close_brackets_positions = [pos for pos, bracket in enumerate(brackets) if bracket == ">"]
    # 2. check if the number of open and close brackets are equal
    if len(open_brackets_positions) != len(close_brackets_positions):
        return False
    # 3. check if each closing bracket is after the corresponding opening bracket
    for closing_bracket_position in close_brackets_positions:
        for opening_bracket_position in open_brackets_positions:
            if opening_bracket_position < closing_bracket_position:
                open_brackets_positions.remove(opening_bracket_position)
                break
        else:
            return False
    return True

