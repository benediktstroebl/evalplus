

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
    # Your code here.
    opening_brackets = ["<", "(", "[", "{"]
    closing_brackets = [">", ")", "]", "}"]

    if len(brackets) == 1:
        return False

    stack = []

    for char in brackets:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack:
                return False
            last_char = stack.pop()
            if not correct_brackets_mapping[last_char] == char:
                return False

    return not stack

