

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
    "*** YOUR CODE HERE ***"
    link_brackets = []
    for i in range(len(brackets)):
        if brackets[i] == "<":
            link_brackets.append("<")
        elif brackets[i] == ">":
            if len(link_brackets) > 0 and link_brackets[-1] == "<":
                link_brackets.pop()
            else:
                return False
    if len(link_brackets) == 0:
        return True
    else:
        return False
