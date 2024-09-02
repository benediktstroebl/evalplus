

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
    pairs = {"(": ")", "{": "}", "[": "]"}
    stack = []
    for char in brackets:
        if char in pairs:
            stack.append(char)
        elif char == pairs[stack.pop()]:
            continue
        else:
            return False
    return not stack
