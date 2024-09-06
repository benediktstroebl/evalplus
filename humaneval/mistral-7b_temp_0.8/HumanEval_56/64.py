

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

    opening_bracket = {"<": ">"}
    brackets_dict = {"<": ">", ">": "<"}

    if len(brackets) % 2 != 0:
        return False
    if brackets[0] != ">":
        return False
    if brackets[-1] != "<":
        return False
    if brackets == ">":
        return True
    elif brackets == "<":
        return True

    stack = []
    for i, bracket in enumerate(brackets):
        if bracket not in opening_bracket:
            return False
        if opening_bracket[bracket] == brackets_dict[bracket]:
            stack.pop()
        else:
            stack.append(bracket)
    if stack:
        return False
    return True


