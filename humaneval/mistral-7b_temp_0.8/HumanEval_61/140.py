

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
    brackets_dict = {
        "(": ")",
        "[": "]",
        "{": "}",
    }

    stack = []
    for ch in brackets:
        if ch in brackets_dict:
            stack.append(ch)
        elif stack and brackets_dict[stack[-1]] == ch:
            stack.pop()
        else:
            return False
    return not stack
