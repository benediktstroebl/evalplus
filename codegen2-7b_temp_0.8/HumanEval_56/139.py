

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
    if not brackets.strip():
        return True
    if not brackets.endswith(">"):
        raise ValueError("brackets should end with '>'")
    opening_brackets = "".join(brackets.split("<"))
    if len(opening_brackets)!= len(set(opening_brackets)):
        return False
    return correct_bracketing(brackets[:-1])
