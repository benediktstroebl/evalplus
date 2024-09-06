

def correct_bracketing(brackets: str):
    """ brackets is a string of "(" and ")".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("(")
    False
    >>> correct_bracketing("()")
    True
    >>> correct_bracketing("(()())")
    True
    >>> correct_bracketing(")(()")
    False
    """

    bracket_map = {
        "(": ")",
        "[": "]",
        "{": "}",
    }
    open_brackets = set(bracket_map.keys())
    closed_brackets = set(bracket_map.values())

    open_stack = []
    for bracket in brackets:
        if bracket in open_brackets:
            open_stack.append(bracket)
        elif bracket in closed_brackets:
            if not open_stack:
                return False
            open_bracket = open_stack.pop()
            if bracket_map[open_bracket]!= bracket:
                return False

    return not open_stack
