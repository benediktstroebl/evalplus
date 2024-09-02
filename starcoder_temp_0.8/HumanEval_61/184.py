

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
    # Your code here
    # 如果输入的字符串为空，则输出False
    if brackets == "":
        return False
    # 栈的初始化
    stack = []
    # 遍历所有字符
    for i in range(len(brackets)):
        if brackets[i] == '(':
            # 将左括号入栈
            stack.append('(')
        else:
            # 将右括号出栈
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    # 如果栈为空则输出True
    if len(stack) == 0:
        return True
    else:
        return False
