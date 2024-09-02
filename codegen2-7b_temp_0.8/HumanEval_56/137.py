

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
    brackets_dict = {'<': '>', '>': '<'}
    stack = []
    for bracket in brackets:
        if bracket in brackets_dict:
            stack.append(bracket)
        else:
            if not stack or brackets_dict[stack.pop()]!= bracket:
                return False
    return not
