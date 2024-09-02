

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

    open_bracket = ["(", "[", "{"]
    closed_bracket = [")", "]", "}"]
    stack = []
    for char in brackets:
        if char in open_bracket:
            stack.append(char)
        elif char in closed_bracket:
            if len(stack) == 0 or closed_bracket.index(char)!= open_bracket.index(stack.pop()):
                return False
    return len(stack) == 0
