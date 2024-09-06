

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
    if not brackets:
        return True
    stack = []
    brackets = brackets.replace('(', ')')
    brackets = brackets.replace(')', '(')
    for i in brackets:
        if i == '(':
            stack.append(i)
        elif stack:
            stack.pop()
    return len(stack) == 0
    
