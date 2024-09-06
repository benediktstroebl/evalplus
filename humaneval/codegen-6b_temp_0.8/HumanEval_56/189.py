

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
    letters = []
    for i in range(len(brackets)):
        if brackets[i] == "<":
            letters.append(">")
        elif brackets[i] == ">":
            if len(letters) == 0:
                return False
            letters.pop() 
    return len(letters) == 0
