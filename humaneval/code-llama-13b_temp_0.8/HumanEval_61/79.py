

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

    # 1. 初始化
    if not brackets:
        return False
    if len(brackets) == 1:
        return False
    count = 0
    # 2. 找出左右括号数量的差值
    for i in range(len(brackets)):
        if brackets[i] == '(':
            count += 1
        else:
            count -= 1
        if count < 0:
            return False
    # 3. 找出左右括号数量的差值
    if count != 0:
        return False
    # 4. 没有错误
    return True

