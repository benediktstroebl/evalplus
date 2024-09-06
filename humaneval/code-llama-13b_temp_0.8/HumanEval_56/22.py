

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

    # NOTE:  DO NOT USE WHILE LOOP

    # Solution 1:  Using for loop
    # ---------------------------------------------
    # stack = []
    # for char in brackets:
    #     if char == "<":
    #         stack.append(char)
    #     else:
    #         if len(stack) == 0:
    #             return False
    #         else:
    #             stack.pop()
    #
    # return len(stack) == 0

    # Solution 2:  Recursion
    # ---------------------------------------------
    if brackets == "":
        return True

    # pop the first character
    char = brackets[0]
    remain = brackets[1:]

    # base case
    if len(remain) == 0:
        return char == ">"
    else:
        return (char == "<" and correct_bracketing(remain)) or \
               (char == ">" and correct_bracketing(remain[1:]))

