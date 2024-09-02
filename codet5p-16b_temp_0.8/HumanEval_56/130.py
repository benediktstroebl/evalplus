

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

    opening_brackets = []
    for i in range(len(brackets)):
        if brackets[i] == '<':
            opening_brackets.append(i)

    closing_brackets = []
    for i in range(len(brackets)):
        if brackets[i] == '>':
            closing_brackets.append(i)

    if len(closing_brackets)!= len(opening_brackets):
        return False

    for i in range(len(opening_brackets)):
        if opening_brackets[i] > closing_brackets[i]:
            return False

    return True

