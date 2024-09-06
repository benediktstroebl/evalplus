

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
    # To begin with, we assume that the brackets are balanced
    if not brackets:
        return True
    elif len(brackets) % 2 != 0:
        return False
    else:
        stack = []
        for bracket in brackets:
            if bracket == ')':
                if not stack:
                    return False
                else:
                    top = stack.pop()
                    if top != '(':
                        return False
            else:
                stack.append(bracket)
        return True

