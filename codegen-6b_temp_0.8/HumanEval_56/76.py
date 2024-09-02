

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
    # This implementation is naive.
    # The only thing that matters is that the stack depth is correct
    bracket_map = {")": "(", "]": "[", "}": "{", ">": "<"}
    stack = []
    for idx, char in enumerate(brackets):
        if char not in bracket_map:
            continue
        if char == ")" and stack and stack[-1] == bracket_map[">"]:
            stack.pop()
        else:
            stack.append(char)
    return not stack
