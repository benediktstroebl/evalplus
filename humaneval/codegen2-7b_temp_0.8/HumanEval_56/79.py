

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
    brackets = brackets.replace("<", "").replace(">", "")
    if len(brackets) % 2!= 0:
        return False
    balanced_brackets = "".join(["<" if b == ">" else ">" for b in brackets])
    return brackets == balanced_br
