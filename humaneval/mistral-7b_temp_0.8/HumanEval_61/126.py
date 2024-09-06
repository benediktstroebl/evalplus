

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
    opening_brackets = "([{"
    closing_brackets = ")]}"

    opening_bracket = {k: v for k, v in zip(opening_brackets, closing_brackets)}

    stack = []
    for char in brackets:
        if char in opening_bracket.keys():
            stack.append(opening_bracket[char])
        elif char in closing_bracket.values():
            if stack:
                last = stack.pop()
                if last != char:
                    return False
            else:
                return False
    return True if not stack else False

