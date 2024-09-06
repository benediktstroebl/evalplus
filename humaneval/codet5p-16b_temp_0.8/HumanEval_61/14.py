

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

    if len(brackets) == 0:
        return True

    bracket_stack = []
    for char in brackets:
        if char == "(" or char == "[":
            bracket_stack.append(char)
        else:
            if len(bracket_stack) == 0:
                return False
            else:
                last_bracket = bracket_stack[-1]
                if last_bracket == "(" and char == ")":
                    bracket_stack.pop()
                elif last_bracket == "[" and char == "]":
                    bracket_stack.pop()
                else:
                    return False
    if len(bracket_stack) == 0:
        return True
    else:
        return False

