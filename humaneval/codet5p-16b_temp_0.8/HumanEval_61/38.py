

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

    stack = []
    bracket_dict = {"(": ")", "{": "}", "[": "]"}
    for bracket in brackets:
        if bracket in bracket_dict.keys():
            stack.append(bracket)
        elif bracket in bracket_dict.values():
            if not stack:
                return False
            current_bracket = stack.pop()
            if bracket_dict[current_bracket]!= bracket:
                return False
    return not stack

