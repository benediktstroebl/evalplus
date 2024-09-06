

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

    opening_bracket = "("
    closing_bracket = ")"
    stack = []
    for ch in brackets:
        if ch == opening_bracket:
            stack.append(ch)
        elif ch == closing_bracket:
            if len(stack) == 0 or stack[-1]!= opening_bracket:
                return False
            else:
                stack.pop()
    return len(stack) == 0
