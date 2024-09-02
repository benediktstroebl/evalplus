

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
    bracket_pairs = {'<':'>', '>':'<', '{':'}', '[':']', '(':')'}
    return len(brackets) % 2 == 0 and all(pair in bracket_pairs for pair in brackets)
