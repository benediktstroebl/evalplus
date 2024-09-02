

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
    if len(brackets) % 2!= 0:
        return False
    
    pairs = zip(brackets, brackets[1:])
    stack = []
    for pair in pairs:
        if pair[0] == '(':
            stack.append(pair[1])
        else:
            if not stack or stack[-1]!= pair[0]:
                return False
            stack.pop()
    return
