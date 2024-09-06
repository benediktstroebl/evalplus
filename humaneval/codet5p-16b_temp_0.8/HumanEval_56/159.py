

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

    stack = []
    brackets = brackets.replace('><', '><').split('<')
    for bracket in brackets:
        if bracket == '':
            continue
        if bracket[0] == '>':
            stack.append(bracket[0])
        else:
            if stack:
                stack.pop()
            else:
                return False
    return len(stack) == 0
