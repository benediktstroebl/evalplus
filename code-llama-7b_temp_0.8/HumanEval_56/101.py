

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
    # open_brackets = 0
    # close_brackets = 0
    # for bracket in brackets:
    #     if bracket == "<":
    #         open_brackets += 1
    #     if bracket == ">":
    #         close_brackets += 1
    #     if open_brackets > close_brackets:
    #         return False
    # if open_brackets == close_brackets:
    #     return True
    # else:
    #     return False
    # return open_brackets == close_brackets
    stack = []
    for i in brackets:
        if i == '(':
            stack.append('(')
        elif i == '[':
            stack.append('[')
        elif i == '{':
            stack.append('{')
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return False
        elif i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                return False
        elif i == '}':
            if stack and stack[-1] == '{':
                stack.pop()
            else:
                return False
        else:
            return False
    return True

