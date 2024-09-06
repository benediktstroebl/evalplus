

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
    if len(brackets) % 2!= 0:
        return False

    left_brackets = re.findall("<[^>]+>", brackets)
    right_brackets = re.findall("[^<]+>", brackets)

    return (left_brackets == right_brackets) and len(left_brackets) > 0
