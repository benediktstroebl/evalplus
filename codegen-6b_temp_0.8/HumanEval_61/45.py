

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
    index_stack = []
    bracket_dict = {"{":"}", "(":")", "[":"]"}

    for bracket in brackets:
        if bracket in bracket_dict:
            index_stack.append(bracket_dict[bracket])
        elif len(index_stack) == 0:
            return False

        if index_stack[-1] != bracket:
            index_stack.pop()
    
    if len(index_stack) == 0:
        return True
    else:
        return False

example = ")()()))"
