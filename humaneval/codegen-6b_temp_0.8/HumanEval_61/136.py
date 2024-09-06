

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
    if len(brackets) % 2 != 0:
        return False
    if len(brackets) <= 1:
        return True
    b_dict = {")": "(", "}": "{", "]": "["}
    stack = []
    for bracket in brackets:
        if bracket in b_dict:
            stack.append(bracket)
        else:
            if len(stack) == 0:
                return False
            else:
                if b_dict[stack[-1]] != bracket:
                    return False
                else:
                    stack.pop()
    if len(stack) == 0:
        return True
    else:
        return False
