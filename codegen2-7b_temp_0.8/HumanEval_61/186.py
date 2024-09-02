

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
    opening_brackets = {'(', '{', '['}
    closing_brackets = {')', '}', ']'}
    stack = []
    for char in brackets:
        if char in opening_brackets:
            stack.append(char)
        elif stack and char == closing_brackets[stack.pop()]:
            pass
        else:
            return False
    return not stack


