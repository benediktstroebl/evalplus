

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
    # 用一个函数实现这个功能，
    # 把它的参数 brackets 看作一个字符串，
    # 函数返回 True 表示 brackets 是合法的括号，False 表示 brackets 是不合法的括号。
    # 函数本身的代码你可以自己写，不要用 built-in function。
    # 你可以用递归、栈、或者其他什么方法来实现。
    # 请仔细阅读下面的评测标准，你的代码将会被自动评测。

    if brackets == "(":
        return False
    elif brackets == ")":
        return False
    elif brackets == "()":
        return True
    else:
        left_bracket = brackets.find("(")
        right_bracket = brackets.rfind(")")
        if left_bracket == right_bracket:
            return False
        else:
            if
