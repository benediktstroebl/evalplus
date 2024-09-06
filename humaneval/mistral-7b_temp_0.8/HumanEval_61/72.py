

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
    opening_brackets = ['(', '{', '[']
    closing_brackets = [')', '}', ']']
    stack = []

    for bracket in brackets:
        if bracket in opening_brackets:
            stack.append(bracket)
        else:
            if not stack:
                return False
            else:
                last_bracket = stack.pop()
                if bracket == closing_brackets[opening_brackets.index(last_bracket)]:
                    continue
                else:
                    return False

    return True if not stack else False

