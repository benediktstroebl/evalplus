

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
    brackets_list = list(brackets)
    if not brackets_list:
        return False

    opening_brackets = ["(", "{", "["]
    closing_brackets = [")", "}", "]"]

    stack = []
    for bracket in brackets_list:
        if bracket in opening_brackets:
            stack.append(bracket)
        else:
            if not stack:
                return False
            opening_bracket = stack.pop()
            if closing_brackets.index(bracket) != opening_brackets.index(opening_bracket):
                return False
    return not stack
