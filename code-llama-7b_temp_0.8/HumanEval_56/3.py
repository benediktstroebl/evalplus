

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

    # List of opening brackets
    open_bracket = ['<', '(', '{']

    # List of closing brackets
    close_bracket = ['>', ')', '}']

    # Check for matching brackets
    stack = []
    for char in brackets:
        if char in open_bracket:
            stack.append(char)
        elif char in close_bracket:
            try:
                if close_bracket.index(char) == open_bracket.index(stack[-1]):
                    stack.pop()
                else:
                    return False
            except IndexError:
                return False
    if len(stack) == 0:
        return True
    return False

