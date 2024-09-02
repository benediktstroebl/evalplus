

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
    brackets = list(brackets)
    if len(brackets) % 2 == 1:
        return False
    else:
        stack = []
        for bracket in brackets:
            if bracket == "(":
                stack.append(bracket)
            else:
                if len(stack) == 0:
                    return False
                else:
                    stack.pop()
        return len(stack) == 0

