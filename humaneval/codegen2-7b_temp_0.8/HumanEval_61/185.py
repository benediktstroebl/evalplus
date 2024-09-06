

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
    
    stack = []
    for character in brackets:
        if character == "(":
            stack.append(character)
        else:
            if not stack or character!= stack.pop():
                return False
    return not stack
