

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
    # return len(brackets) % 2 == 0
    pairs = {
        "<": ">",
        ">": "<",
        "{": "}",
        "}": "{",
        "[": "]",
        "]": "[",
        "(": ")",
        ")": "(",
    }
    stack = []
    for c in brackets:
        if c in pairs:
            stack.append(c)
        else:
            if stack == []:
                return False
            else:
                if pairs[stack[-1]] == c:
                    stack.pop()
                else:
                    return False
    return len(stack) == 0

