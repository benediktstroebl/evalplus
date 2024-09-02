

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
    stack = []
    for opening in brackets:
        if stack and stack[-1] != ')' and openings[stack[-1]][1] != '(':
            return False
        stack.append(opening)
    return stack.pop() == ')'