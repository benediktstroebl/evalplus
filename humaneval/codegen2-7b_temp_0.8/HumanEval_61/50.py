

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
    if brackets.count('(')!= brackets.count(')'):
        return False
    brackets = brackets[1:-1]
    opens = list()
    for char in brackets:
        if char == '(':
            opens.append(char)
        elif char in opens:
            opens.remove(char)
        else:
            return False
    return True

