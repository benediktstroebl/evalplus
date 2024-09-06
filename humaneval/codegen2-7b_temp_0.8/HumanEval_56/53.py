

def correct_bracketing(brackets: str):
    """ brackets is a string of "<" and ">".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("<")
    False
    >>> correct_bracketing("<>")
    True
    >>> correct_bracketing("<<><>>")
    True
    >>> correct_bracketing("><<>")
    False
    """
    opening_brackets = {
        '<': '>',
        '{': '}',
        '[': ']',
        '(': ')',
    }
    stack = []
    for bracket in brackets:
        if bracket in opening_brackets:
            stack.append(bracket)
        else:
            if not stack or opening_brackets[stack.pop()]!= bracket:
                return False
    return
