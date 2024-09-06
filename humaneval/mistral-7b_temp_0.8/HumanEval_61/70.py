

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
    bracket_dict = {"(": ")", "[": "]", "{": "}"}
    bracket_stack = []

    for bracket in brackets:
        if bracket in bracket_dict:
            bracket_stack.append(bracket_dict[bracket])
        elif bracket == bracket_stack.pop():
            continue
        else:
            return False

    return True
