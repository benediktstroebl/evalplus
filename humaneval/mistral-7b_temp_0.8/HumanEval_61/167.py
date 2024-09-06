

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

    # Write your code here
    # 在这里添加你的代码

    brackets_list = list(brackets)
    print(brackets_list)

    for i in range(len(brackets_list)):
        if brackets_list[i] == '(':
            brackets_list[i] = 'l'
        else:
            brackets_list[i] = 'r'
    print(brackets_list)

    # 如果这个字符串是正确括号，
    # 那么在这个数组中，在每个左括号后面都会有一个右括号。
    for i in range(len(brackets_list)):
        if brackets_list[i] == 'l' and brackets_list[i + 1] != 'r':
            return False
    return True

