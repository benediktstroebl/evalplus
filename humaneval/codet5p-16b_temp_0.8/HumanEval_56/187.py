

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

    open_brackets = ["<"]
    close_brackets = [">"]

    bracket_map = {brackets[0]: close_brackets[0]}

    for i in range(1, len(brackets)):
        if brackets[i] in open_brackets:
            bracket_map[brackets[i]] = close_brackets[0]
        elif brackets[i] in close_brackets:
            if bracket_map.get(brackets[i])!= close_brackets[0]:
                return False
            bracket_map[brackets[i]] = close_brackets[1]
        else:
            return False
    for open_bracket in open_brackets:
        if bracket_map.get(open_bracket)!= close_brackets[0]:
            return False

    return True
