

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
    
    opening_brackets = brackets.count("<")
    
    bracket_pairs = [b for b in zip(brackets, brackets[1:]) if b[0] == "<" and b[1] == ">"]

    if len(bracket_pairs) % 2 == 1:
        return False

    return opening_brackets == len(bracket_pairs)
