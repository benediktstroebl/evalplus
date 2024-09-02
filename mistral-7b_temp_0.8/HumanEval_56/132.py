

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

    # 括号首尾必须匹配
    assert brackets[0] == '<' and brackets[-1] == '>'

    # 剩余部分
    brackets = brackets[1:-1]

    if not brackets:
        return True

    stack = []
    for ch in brackets:
        if ch == '<':
            stack.append(ch)
        elif ch == '>':
            if not stack:
                return False
            stack.pop()
    return not stack

