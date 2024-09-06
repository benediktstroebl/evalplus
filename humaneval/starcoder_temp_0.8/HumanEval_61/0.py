

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
    s = Stack()
    for char in brackets:
        if char == '(':
            s.push(char)
        elif char == ')':
            if s.is_empty():
                return False
            else:
                s.pop()
    return s.is_empty()
