

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

    bracket_stack = []
    open_brackets = set(['(', '[', '{'])
    closed_brackets = set([')', ']', '}'])

    for char in brackets:
        if char in open_brackets:
            bracket_stack.append(char)
        elif char in closed_brackets:
            if len(bracket_stack) == 0 or bracket_stack.pop()!= char:
                return False
    return len(bracket_stack) == 0
