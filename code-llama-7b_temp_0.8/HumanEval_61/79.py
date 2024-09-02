

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
    # Write your code here!
    if brackets == "":
        return True
    stack = []
    for b in brackets:
        if b == "(":
            stack.append("(")
        elif b == ")":
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    return len(stack) == 0


