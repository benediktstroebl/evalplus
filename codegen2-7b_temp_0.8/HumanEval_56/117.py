

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
    brackets = brackets.split()
    for i in range(len(brackets)):
        if brackets[i]!= ">":
            if i + 1 == len(brackets):
                return False
            else:
                if brackets[i + 1]!= "<":
                    return False
    
