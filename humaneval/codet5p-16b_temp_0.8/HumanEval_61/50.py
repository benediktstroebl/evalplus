

def correct_bracketing(brackets: str):
    """ brackets is a string of "(" and ")".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("(")
    False
    >>> correct_bracketing("()")
    True
    >>> correct_bracketing("(()())")
    True
    >>> correct_bracketing(")(()")
    False
    """

    stack = []
    open_brackets = ["(", "[", "{"]
    for char in brackets:
        if char in open_brackets:
            stack.append(char)
        else:
            if len(stack) == 0:
                return False
            else:
                if stack[-1] == "(" and char == ")":
                    stack.pop()
                elif stack[-1] == "{" and char == "}":
                    stack.pop()
                elif stack[-1] == "[" and char == "]":
                    stack.pop()
                else:
                    return False

    if len(stack) == 0:
        return True
    else:
        return False
