

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
    bracket_pairs = {"(": ")", "{": "}", "[": "]"}
    for char in brackets:
        if char in bracket_pairs:
            bracket_stack.append(char)
        else:
            if not bracket_stack:
                return False
            top = bracket_stack.pop()
            if bracket_pairs[top]!= char:
                return False
    return not bracket_stack
    
