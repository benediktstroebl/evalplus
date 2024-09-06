

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
    brackets_list = brackets.split(">")

    if len(brackets_list) % 2!= 0:
        return False

    correct = True

    for idx, bracket in enumerate(brackets_list):
        if bracket!= ">>":
            if idx % 2 == 1:
                correct = False
                break
    return
