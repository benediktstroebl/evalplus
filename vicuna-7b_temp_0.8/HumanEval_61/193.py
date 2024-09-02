

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
    # Split the string into lists of open and close brackets
    open, close = [], []
    for char in brackets:
        if char == '(':
            open.append(char)
        else:
            close.append(char)
    if len(open) != len(close):
        return False
    # Iterate over the lists of open and close brackets
    for i in range(len(open)):
        if open[i] != close[i]:
            return False
    return True
