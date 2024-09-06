

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
    open_brackets = {"(", "[", "{"}

    opening_bracket_stack = []
    for bracket in brackets:
        if bracket in open_brackets:
            opening_bracket_stack.append(bracket)
        else:
            if len(opening_bracket_stack) <= 0:
                return False
            elif bracket == ")" and opening_bracket_stack.pop() != "(":
                return False

            elif bracket == "]" and opening_bracket_stack.pop() != "[":
                return False

            elif bracket == "}" and opening_bracket_stack.pop() != "{":
                return False

    return True

