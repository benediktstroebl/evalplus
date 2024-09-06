

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
    # 新建两个栈
    stack = []
    closing = {"<": ">", ">": "<"}
    for b in brackets:
        # 如果是左括号就进栈
        if b in "<>":
            stack.append(b)
        # 如果是右括号就取出栈顶元素，判断是否一致
        else:
            if not stack or closing[stack.pop()] != b:
                return False
    return not stack

