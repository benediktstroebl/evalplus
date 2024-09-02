

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
    # Your code here
    opening = 0
    closing = 0
    for i in range(len(brackets)):
        if brackets[i] == '<':
            opening += 1
        elif brackets[i] == '>':
            closing += 1
        if closing > opening:
            return False
    return closing == opening

