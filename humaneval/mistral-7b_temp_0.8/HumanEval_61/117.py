

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
    openers = {"(": ")", "[": "]", "{": "}"}
    stack = []
    for i, c in enumerate(brackets):
        if c in openers.values():
            if len(stack) != 0 and openers[stack[-1]] == c:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)

    return len(stack) == 0
