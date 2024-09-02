

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
    # language-agnostic solution (no string methods):
    #
    # def correct_bracketing(brackets):
    #     num_open = 0
    #     for char in brackets:
    #         if char == '<':
    #             num_open += 1
    #         elif char == '>':
    #             num_open -= 1
    #         if num_open < 0:
    #             return False
    #     return num_open == 0

    # pythonic solution (string methods):
    #
    # return brackets.count('<') == brackets.count('>')

    # typical pythonic solution:
    return brackets.count('<') == brackets.count('>')




