

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
    open_brackets = "{}[]()"
    bracket_pairs = {"{": "}", "[": "]", "(": ")"}
    stack = []
    for bracket in brackets:
        if bracket in open_brackets:
            stack.append(bracket)
        else:
            if stack:
                last_opening_bracket = stack.pop()
                if last_opening_bracket != bracket_pairs[bracket]:
                    return False
            else:
                return False
    if stack:
        return False
    return True

