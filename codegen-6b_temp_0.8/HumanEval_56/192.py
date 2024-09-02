

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
    brackets = brackets.split("<");
    if len(brackets) != len(">"):
        return False
        
    return all(">" + b + "<" == c for b,c in zip(brackets[1:], brackets[:-1]))
